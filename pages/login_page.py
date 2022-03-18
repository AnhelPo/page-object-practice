'''
Class for the login page.
'''

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
                "URL does not contain the word 'login'!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), \
                "In LOG IN form field for EMAIL is missing!"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), \
                "In LOG IN form field for PASSWORD is missing!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), \
                "In LOG IN form BUTTON is missing!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTER), \
                "In REGISTRATION form field for EMAIL is missing!"
        assert self.is_element_present(*LoginPageLocators.PASSWORD1_REGISTER), \
                "In REGISTRATION form FIRST field for PASSWORD is missing!"
        assert self.is_element_present(*LoginPageLocators.PASSWORD2_REGISTER), \
                "In REGISTRATION form SECOND field for PASSWORD is missing!"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), \
                "In REGISTRATION form BUTTON is missing!"
