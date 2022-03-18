'''
Tests for the main page.
Checks:
    - login link exists,
    - guest user can go to the login page from the main page.
'''

from pages.main_page import MainPage

URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, URL)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
