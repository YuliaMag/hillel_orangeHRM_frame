from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    DASHBOARD_PAGE = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]')

