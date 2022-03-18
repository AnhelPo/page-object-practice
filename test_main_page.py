'''
Tests for the main page.
Checks out:
    - guest user can go to login page from the main page.
'''

from pages.main_page import MainPage


URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    URL = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, URL)
    page.open()
    page.go_to_login_page()
