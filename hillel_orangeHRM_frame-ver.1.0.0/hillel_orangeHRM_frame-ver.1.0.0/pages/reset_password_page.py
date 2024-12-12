from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class ResetPasswordPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    RESET_PASSWORD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
    USER_NAME = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
    RESET_PASSWORD_FORM = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')





