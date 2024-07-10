from selenium.webdriver.common.by import By
import pages.base_page


class ResetPasswordPage(pages.base_page.BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USER_NAME = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
    RESET_PASSWORD_FORM = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[1]')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')

    RESET_PASSWORD_LINK = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')

    @property
    def cancel_button(self):
        return self.find_element(ResetPasswordPage.CANCEL_BUTTON)

    @property
    def reset_password_button(self):
        return self.find_element(ResetPasswordPage.RESET_PASSWORD_BUTTON)

    @property
    def reset_password_link(self):
        return self.find_element(ResetPasswordPage.RESET_PASSWORD_LINK)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_reset_password_button(self):
        self.reset_password_button.click()

    def display_reset_password_link(self):
        self.click_reset_password_button()
        return self.reset_password_link()


