import time
import pytest
from selenium.webdriver.common.by import By


def test_successful_login(browser):
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
    dashboard_page = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]')

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" in browser.current_url  # full link with host is bad practice!
    assert dashboard_page.is_displayed(), ""


if __name__ == "__main__":
    pytest.main()
