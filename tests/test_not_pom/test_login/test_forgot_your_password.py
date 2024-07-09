import time
import pytest
from selenium.webdriver.common.by import By


def test_forgot_your_password(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    forgot_your_password_button = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div['
                                                                 '2]/form/div[4]/p')
    forgot_your_password_button.click()
    time.sleep(1)
    reset_password = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')

    assert ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
            in browser.current_url)  # full link with host is bad practice!
    assert reset_password.is_displayed(), ""


if __name__ == "__main__":
    pytest.main()
