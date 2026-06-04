import pytest
import time
import traceback
from datetime import datetime
import mysql.connector
from selenium import webdriver
from dotenv import load_dotenv
import os
import uuid


# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Retrieve the secrets using os.getenv()
selenium_grid_url = os.getenv("SELENIUM_GRID_URL")
mysql_url = os.getenv("MYSQL_URL")
mysql_username = os.getenv("MYSQL_USERNAME")
mysql_password = os.getenv("MYSQL_PASSWORD")

GRID_URL = selenium_grid_url

COMMON_ARGS = [
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--window-size=1920,1080",
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

def pytest_configure(config):
    # Only the master process creates the RunID
    if not hasattr(config, "workerinput"):
        config.run_id = str(uuid.uuid4())


def pytest_configure_node(node):
    # Send the RunID to each worker
    node.workerinput["run_id"] = node.config.run_id


def pytest_sessionstart(session):
    # Workers receive the RunID here
    if hasattr(session.config, "workerinput"):
        session.config.run_id = session.config.workerinput["run_id"]

def make_options(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    elif browser == "edge":
        options = webdriver.EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    for arg in COMMON_ARGS:
        options.add_argument(arg)

    return options

def log_test_result(result):
    conn = mysql.connector.connect(
        host=mysql_url,
        user=mysql_username,
        password=mysql_password,
        database="selenium"
    )

    cursor = conn.cursor()

    query = """
        INSERT INTO seleniumgrid_docker_cnn
        (run_id, worker_id, test_name, status, error_message, browser, node, start_time, end_time, duration_ms)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        result["run_id"],
        result["worker_id"],
        result["test_name"],
        result["status"],
        result["error_message"],
        result["browser"],
        result["node"],
        result["start_time"],
        result["end_time"],
        result["duration_ms"]
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param
    options = make_options(browser)

    d = webdriver.Remote(command_executor=GRID_URL, options=options)

    # Attach metadata for logging
    d.test_meta = {
        "browser": browser,
        "node": GRID_URL,
        "start_time": datetime.now(),
        "start_ts": time.time()
    }

    yield d
    d.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver = item.funcargs.get("driver", None)
    if not driver:
        return

    end_time = datetime.now()
    duration_ms = int((time.time() - driver.test_meta["start_ts"]) * 1000)
    worker_id = getattr(item.config, "workerinput", {}).get("workerid", "master")

    result = {
        "run_id": item.config.run_id,
        "worker_id": worker_id,
        "test_name": item.name,
        "status": "PASS" if report.passed else "FAIL",
        "error_message": None if report.passed else str(report.longrepr),
        "browser": driver.test_meta["browser"],
        "node": driver.test_meta["node"],
        "start_time": driver.test_meta["start_time"],
        "end_time": end_time,
        "duration_ms": duration_ms
    }

    log_test_result(result)