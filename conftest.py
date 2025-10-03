
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome or firefox")
    parser.addoption("--base-url", action="store", default="https://www.demoblaze.com/")
    parser.addoption("--headed", action="store_true", help="Run with browser UI")
    parser.addoption("--wait", action="store", default="10", help="Default explicit wait seconds")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url")

@pytest.fixture(scope="session")
def wait_seconds(pytestconfig):
    return int(pytestconfig.getoption("--wait"))

@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("--browser").lower()

@pytest.fixture(scope="session")
def driver(pytestconfig, browser_name):
    headed = pytestconfig.getoption("--headed")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if not headed:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        options = ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,900")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(0)
    driver.set_page_load_timeout(60)
    yield driver
    driver.quit()
