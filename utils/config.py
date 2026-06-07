from dotenv import load_dotenv
import os

load_dotenv()

SELENIUM_GRID_URL = os.getenv("SELENIUM_GRID_URL")

MYSQL_URL = os.getenv("MYSQL_URL")
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")