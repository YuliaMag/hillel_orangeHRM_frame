import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

driver_path = 'C:/Selenium/chromedriver.exe'


@pytest.fixture()
def browser():
    # driver = Chrome()
    driver = Chrome(service=Service(driver_path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

