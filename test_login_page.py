'''
Tests for the login page.
Checks:
    - current url contains the word "login",
    - all fields for log in exist on page,
    - a button for log in exists on page,
    - all fields for registration exist on page,
    - a button for registration exists on page.
'''

from pages.login_page import LoginPage

URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_url_is_correct_and_forms_for_login_and_registration_exist(browser):
    page = LoginPage(browser, URL)
    page.open()
    page.should_be_login_page()
