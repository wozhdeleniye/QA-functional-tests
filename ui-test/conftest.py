import pytest

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

BASE_URL = "http://127.0.0.1:5000/"


@pytest.fixture
def browser():
    options = EdgeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")

    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(BASE_URL)

    yield driver

    driver.quit()