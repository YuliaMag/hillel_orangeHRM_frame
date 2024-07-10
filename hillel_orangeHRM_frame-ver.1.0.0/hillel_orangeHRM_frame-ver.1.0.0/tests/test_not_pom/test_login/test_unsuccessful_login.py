import time
import pytest
from selenium.webdriver.common.by import By


def test_unsuccessful_login(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username_name = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div["
                                                  "3]/button")

    username_name.send_keys("Admin")
    password_input.send_keys("wrongpass###")
    time.sleep(1)
    login_button.click()
    time.sleep(1)
    error_msg = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" in browser.current_url  # full link with host is bad practice!
    assert error_msg.is_displayed(), ""


if __name__ == "__main__":
    pytest.main()



