import time
import pytest
from selenium.webdriver.common.by import By


def test_item_click_performance(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username_name = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div["
                                                  "3]/button")

    username_name.send_keys("Admin")
    password_input.send_keys("admin123")
    time.sleep(1)
    login_button.click()
    time.sleep(1)

    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    performance_tab_button = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li['
                                                            '7]/a/span')
    time.sleep(1)
    performance_tab_button.click()
    time.sleep(1)
    performance_tab = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]')

    assert performance_tab.is_displayed(), ""


if __name__ == "__main__":
    pytest.main()
