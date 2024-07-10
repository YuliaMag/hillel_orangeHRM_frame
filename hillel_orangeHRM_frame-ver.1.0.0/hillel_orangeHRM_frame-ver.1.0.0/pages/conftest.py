"""
To implement initialization for WebDriver
"""

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

driver_path = 'C:/Selenium/chromedriver.exe'


@pytest.fixture() #(scope="session") -- ??
def browser():
    driver = Chrome(service=Service(driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()
