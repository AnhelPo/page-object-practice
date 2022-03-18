'''
Contains locators for all elements in project.
'''

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LOCATOR = (By.ID, "login_link")


class LoginPageLocators():
    EMAIL_LOGIN = (By.ID, "id_login-username")
    PASSWORD_LOGIN = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    EMAIL_REGISTER = (By.ID, "id_registration-email")
    PASSWORD1_REGISTER = (By.ID, "id_registration-password1")
    PASSWORD2_REGISTER = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
