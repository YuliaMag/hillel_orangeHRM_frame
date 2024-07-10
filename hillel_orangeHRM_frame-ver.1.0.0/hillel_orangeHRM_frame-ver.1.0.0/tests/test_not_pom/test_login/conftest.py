import time
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


# @pytest.fixture()
# def scroller():
#     SCROLL_PAUSE_TIME = 0.5
#     driver = Chrome(service=Service(driver_path))
#     last_height = driver.execute_script("return document.body.scrollHeight")
#
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#         time.sleep(SCROLL_PAUSE_TIME)
#
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height
#
#
#    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
