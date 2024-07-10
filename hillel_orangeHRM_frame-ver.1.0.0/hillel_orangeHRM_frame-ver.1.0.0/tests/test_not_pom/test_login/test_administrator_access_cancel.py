import time
import pytest
from selenium.webdriver.common.by import By


def test_administrator_access_cancel(browser):
    # login
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

    # maintenance tab
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    maintenance_tab_button = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li['
                                                            '10]/a/span')
    time.sleep(1)
    maintenance_tab_button.click()
    time.sleep(1)
    maintenance_form = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]')

    assert maintenance_form.is_displayed(), ""

    # admin check
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee")

    cancel_button = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[1]')
    time.sleep(1)
    cancel_button.click()
    time.sleep(1)

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" in browser.current_url


if __name__ == "__main__":
    pytest.main()
