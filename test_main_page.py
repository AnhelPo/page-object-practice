'''
Tests for the main page.
Checks:
    - login link exists,
    - guest user can go to the login page from the main page,
    - login page has correct URL and contains correct forms for
      log in and registration.
'''

from pages.main_page import MainPage
from pages.login_page import LoginPage

URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, URL)
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
