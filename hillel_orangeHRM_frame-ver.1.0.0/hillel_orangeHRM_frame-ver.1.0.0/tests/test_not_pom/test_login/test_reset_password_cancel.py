import time
import pytest
from selenium.webdriver.common.by import By


def test_reset_password_cancel(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")

    cancel_button = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[1]')

    cancel_button.click()
    time.sleep(1)

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" in browser.current_url  # full link with host is bad practice!


if __name__ == "__main__":
    pytest.main()
