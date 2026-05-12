import pytest
import os
from selenium import webdriver

if "var/lib/jenkins/workspace" in os.getcwd():
    print("We are running script from Jenkins server")
    GRID_URL = "http://192.168.150.1:4444"
    print("GRID URL is ", GRID_URL)
else:
    print("We are running script from outside of the Jenkins server")
    GRID_URL = "http://192.168.150.1:4444"
    print("Path for results file has been set, type set to manual")
    print("GRID URL is ", GRID_URL)

COMMON_ARGS = [
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--window-size=1920,1080",
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

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


@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param
    options = make_options(browser)
    d = webdriver.Remote(command_executor=GRID_URL, options=options)
    yield d
    d.quit()

def test_cnn_loads(driver):
    driver.get("https://www.cnn.com")
    print(f"\nBrowser: {driver.capabilities['browserName']} | Title: {driver.title}")
    assert "CNN" in driver.title

def test_cnn_title_not_empty(driver):
    driver.get("https://www.cnn.com")
    assert len(driver.title) > 0

def test_cnn_url(driver):
    driver.get("https://www.cnn.com")
    assert "cnn.com" in driver.current_url

def test_cnn_redirects_to_https(driver):
    driver.get("http://www.cnn.com")
    assert driver.current_url.startswith("https")