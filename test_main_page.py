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
    # check for login link existence on the main page
    main_page.should_be_login_link()
    # go to the login page
    main_page.go_to_login_page()

    # browser.current_url has changed to login page URL
    login_page = LoginPage(browser, browser.current_url)
    # check for correct URL and forms for log in and registration
    login_page.should_be_login_page()
