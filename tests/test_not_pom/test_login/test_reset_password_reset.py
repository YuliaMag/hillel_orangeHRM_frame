import time
import pytest
from selenium.webdriver.common.by import By


def test_reset_password_reset(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")

    reset_password_button = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
    username_name = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')

    username_name.send_keys("Admin")
    time.sleep(1)
    reset_password_button.click()
    time.sleep(1)

    reset_password_link_sent_successfully = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')

    assert reset_password_link_sent_successfully.is_displayed(), ""
    assert ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
            in browser.current_url)  # full link with host is bad practice!


if __name__ == "__main__":
    pytest.main()
