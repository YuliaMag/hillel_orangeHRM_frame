from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USERNAME_INPUT_FIELD = (By.ID, "username")
    PASSWORD_INPUT_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[""3]/button")
    FORGOT_YOUR_PASSWORD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[''2]/form/div[4]/p')
    ERROR_MSG = (
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')  # "Invalid credentials"

    @property
    def username_input_field(self):
        return self.find_element(LoginPage.USERNAME_INPUT_FIELD)

    @property
    def password_input_field(self):
        return self.find_element(LoginPage.PASSWORD_INPUT_FIELD)

    @property
    def login_button(self):
        return self.find_element(LoginPage.LOGIN_BUTTON)

    @property
    def forgot_your_password_button(self):
        return self.find_element(LoginPage.FORGOT_YOUR_PASSWORD_BUTTON)

    @property
    def error_message(self):
        return self.find_element(LoginPage.ERROR_MSG)

    def is_displayed(self):
        return self.login_button.is_displayed()

    def username_input(self, user):
        self.username_input_field.send_keys(user.username)
        return self

    def password_input(self, user):
        self.password_input_field.send_keys(user.password)
        return self

    def click_login_button(self):
        self.login_button.click()

    def click_forgot_your_password_button(self):
        self.forgot_your_password_button.click()

    def login_with_credentials(self, user):
        self.username_input(user)
        self.password_input(user)
        self.click_login_button()

    def perform_successful_login(self, user):
        from pages.dashboard_page import DashboardPage
        self.login_with_credentials(user)
        return DashboardPage(self.driver)

    def perform_unsuccessful_login(self, user):
        self.login_with_credentials(user)
        return self

    def perform_forgot_your_password_redirect(self):
        from pages.reset_password_page import ResetPasswordPage
        self.click_forgot_your_password_button()
        return ResetPasswordPage(self.driver)

    def show_error_msg(self):
        self.error_message()
        return self
