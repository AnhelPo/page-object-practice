"""
Tests for the main page.

Checks:
 - login link exists on the main page,
 - guest user can go to the login page from the main page,
 - login page has correct URL and contains correct forms for
   log in and registration,
 - basket link exists on the main page,
 - guest user can go to the basket page from the main page,
 - if no item was added to basket by guest user, the basket is empty
   and a message about empty basket is shown.

!! Tests are intentionally grouped by theme, not in alphabetical order.
"""

import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

URL = "http://selenium1py.pythonanywhere.com/"


def get_class_instance_and_open_page(browser):
    """
    Helper function for all functions to implement
    DRY principle. Is called only from tests.
    """
    page = MainPage(browser, URL)
    page.open()
    return page


@pytest.mark.login_from_main_page
class TestGuestGoToLoginFromMainPage:

    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        """
        Check if guest user can:
         - see login link on the main page,
         - go to the login page from the main page.
         !! 2 stepik tests are in one for code consistency:
          * test_guest_should_see_login_link and
          * test_guest_can_go_to_login_page.
         """
        # see above here the helper function
        main_page = get_class_instance_and_open_page(browser)

        # check for login link existence on the main page;
        # BasePage method
        main_page.should_be_login_link()

        # go to the login page; BasePage method
        main_page.go_to_login_page()

        # browser.current_url has changed to login page URL;
        # new page should be a LoginPage instance
        login_page = LoginPage(browser, browser.current_url)

        # check for correct URL and forms for login and registration;
        # LoginPage method
        login_page.should_be_login_page()


@pytest.mark.guest_check_basket_from_main_page
class TestGuestCheckBasketFromMainPage:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        """
        Check if guest user can:
        - see basket link on the main page,
        - go to the basket page from the main page,
        - (if no item was added to basket) see empty basket on basket page,
        - (if no item was added to basket) see a message about an empty
          basket on basket page.
        """
        # see above here the helper function
        main_page = get_class_instance_and_open_page(browser)

        # check for basket link existence on the main page;
        # BasePage method
        main_page.should_be_basket_link()

        # go to the basket page; BasePage method
        main_page.go_to_basket_page()

        # browser.current_url has changed to basket page URL;
        # new page should be a BasketPage instance
        basket_page = BasketPage(browser, browser.current_url)

        # check for no items in basket;
        # BasketPage method
        basket_page.should_not_be_items_is_basket()

        # check for message "Your basket is empty";
        # BasketPage method
        basket_page.should_be_message_about_empty_basket()
