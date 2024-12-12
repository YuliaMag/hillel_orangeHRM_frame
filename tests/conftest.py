import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from helpers.user import User
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.dashboard_page import DashboardPage


driver_path = 'C:/Selenium/chromedriver.exe'


@pytest.fixture()
def browser():
    driver = Chrome(service=Service(driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def valid_user():
    return User("Admin", "admin123")


@pytest.fixture(scope='session')
def invalid_user():
    return User("Admin", "wrongpass###")


@pytest.fixture()
def login_page(browser):
    return LoginPage(browser).navigate()


@pytest.fixture()
def reset_page(browser):
    return ResetPasswordPage(browser).navigate()


@pytest.fixture()
def dashboard_page(browser):
    return DashboardPage(browser).navigate()

