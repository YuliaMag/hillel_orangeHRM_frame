from helpers.project_helpers import get_base_url
from pages import reset_password_page
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USERNAME_INPUT_FIELD = (By.ID, "username")
    PASSWORD_INPUT_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[""3]/button")
    FORGOT_YOUR_PASSWORD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[''2]/form/div[4]/p')

    @property
    def username_input_field(self):
        return self.find_element(LoginPage.USERNAME_INPUT_FIELD)

    @property
    def password_input_field(self):
        return self.find_element(LoginPage.PASSWORD_INPUT_FIELD)

    @property
    def login_button(self):
        return self.find_element(LoginPage.LOGIN_BUTTON)

    def forgot_your_password_button(self):
        return self.find_element(LoginPage.FORGOT_YOUR_PASSWORD_BUTTON)

    def navigate(self):
        self.driver.get(get_base_url())
        return self

    def is_displayed(self):
        return self.login_button.is_displayed()

    def enter_username(self, user):
        self.username_input_field.send_keys(user.username)
        return self

    def enter_password(self, user):
        self.password_input_field.send_keys(user.password)
        return self

    def click_login_button(self):
        self.login_button.click()

    def click_forgot_your_password_button(self):
        self.forgot_your_password_button.click()

    def fill_credentials_and_click_login_button(self, user):
        self.enter_username(user)
        self.enter_password(user)
        self.click_login_button()

    def perform_successful_login(self, user):
        self.fill_credentials_and_click_login_button(user)
        return DashboardPage(self.driver)

    def perform_unsuccessful_login(self, user):
        self.fill_credentials_and_click_login_button(user)
        return self

    def perform_forgot_your_password_redirect(self, user):
        self.click_forgot_your_password_button()
        return reset_password_page.ResetPasswordPage(self.driver)



