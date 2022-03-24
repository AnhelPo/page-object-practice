"""
Tests for product page.

Checks:
 - button for adding item to the shopping basket exists on page
   and is clickable,
 - after click on button for adding item to the basket:
        * the name of item in the basket matches the name of chosen item,
        * the price of item in the basket matches the price of chosen item,
        * after adding item to basket success message appears,
 - login link exists on product page,
 - guest user can go to the login page from the product page,
 - login page has correct URL and contains correct forms for
   log in and registration,
 - basket link exists on product page,
 - guest user can go to the basket page from the product page,
 - if no item was added to basket by guest user, the basket is empty
   and a message about empty basket is shown,
 - registered user can go to the basket page from the product page,
 - if no item was added to basket by registered user, the basket is empty
   and a message about empty basket is shown.

!! Tests are intentionally grouped by theme, not in alphabetical order.
"""

import time
import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

URL_PRODUCT = '''http://selenium1py.pythonanywhere.com/
catalogue/the-city-and-the-stars_95/'''
URL_LOGIN = "http://selenium1py.pythonanywhere.com/accounts/login/"


def get_class_instance_and_open_page(browser):
    """
    Helper function for all functions to implement
    DRY principle. Is called only from tests.
    """
    page = ProductPage(browser, URL_PRODUCT)
    page.open()
    return page


def generate_email_and_password():
    """
    Prepare data for registration of a new user.
    """
    # e.g. 52.2906601@fakemail.org
    email = str(time.time())[-10:] + "@fakemail.org"

    # e.g. 203.150016
    password = str(time.time())[-10:]
    return email, password


@pytest.mark.login_from_product_page
class TestGuestGoToLoginFromProductPage:

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        """
        Check if guest can:
         - see login link on the product page,
         - go to the login page from the product page.
         !! 2 tests are in one for code consistency:
         * test_guest_should_see_login_link and
         * test_guest_can_go_to_login_page.
        """
        # see above here the helper function
        product_page = get_class_instance_and_open_page(browser)

        # check for login link existence on product page;
        # BasePage method
        product_page.should_be_login_link()

        # go to the login page; BasePage method
        product_page.go_to_login_page()

        # browser.current_url has changed to login page URL;
        # new page should be a LoginPage instance
        login_page = LoginPage(browser, browser.current_url)

        # check for correct URL and forms for log in and registration;
        # LoginPage method
        login_page.should_be_login_page()


@pytest.mark.guest_add_to_basket
class TestGuestAddToBasketFromProductPage:

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        """
        Check:
         - guest user can see button for adding item to basket,
         - guest user can click on button for adding item to basket,
         - item is in the basket after adding,
         - item's name and price in the basket matches chosen one.
        """
        # see above here the helper function
        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence
        page.should_be_button_for_adding_to_basket()

        # check for button "Add to basket" clickability
        page.should_be_clickable_button_for_adding_to_basket()

        # check for success message after adding item to basket
        page.should_be_success_message_after_adding_to_basket()

        # check for adding item to basket with the same name
        page.should_be_correct_item_in_basket_after_adding()

        # check for adding item to basket with the same price
        page.should_be_correct_price_in_basket_after_adding()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        Check that no success message is shown to guest AFTER
        adding item to basket.
        """
        # see above here the helper function
        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence and clickability
        page.should_be_clickable_button_for_adding_to_basket()

        # check for no message is shown
        page.should_not_be_success_message_after_adding_item_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        """
        Check that no success message is shown BEFORE
        adding item to basket.
        """
        # see above here the helper function
        page = get_class_instance_and_open_page(browser)

        # check for no message is shown
        page.should_not_be_success_message_before_adding_item_to_basket()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        """
        Check that message about successful adding item to basket disappeares.
        """
        # see above here the helper function
        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence and clickability
        page.should_be_clickable_button_for_adding_to_basket()

        # check for message disappearance
        page.should_message_disappear_after_adding_product_to_basket()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        """
        Check if guest user can:
        - see basket link on the main page,
        - go to the basket page from the main page,
        - (if no item was added to basket) see empty basket on basket page,
        - (if no item was added to basket) see a message about an empty
          basket on basket page.
        """
        # see above here the helper function
        product_page = get_class_instance_and_open_page(browser)

        # check for basket link existence on the main page; BasePage method
        product_page.should_be_basket_link()

        # go to the basket page; BasePage method
        product_page.go_to_basket_page()

        # browser.current_url has changed to basket page URL;
        # new page should be a BasketPage instance
        basket_page = BasketPage(browser, browser.current_url)

        # check for no items in basket;
        # BasketPage method
        basket_page.should_not_be_items_is_basket()

        # check for message "Your basket is empty";
        # BasketPage method
        basket_page.should_be_message_about_empty_basket()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Register a new user and check log in.
        """
        # get class instance and open page
        login_page = LoginPage(browser, URL_LOGIN)
        login_page.open()

        # see above here the function for data generation
        email, password = generate_email_and_password()

        # guest registers as a new user;
        # LoginPage method
        login_page.register_new_user(email, password)

        # check the appearence of the user icon;
        # BasePage method
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """
        Check that no message is shown before adding item to basket.
        """
        # see above here the helper function
        page = get_class_instance_and_open_page(browser)

        # check for no message is shown
        page.should_not_be_success_message_before_adding_item_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Check:
         - registered user can see button for adding item to basket,
         - registered user can click on button for adding item to basket,
         - success message is shown after adding item to basket,
         - item's name and price in the basket matches name and price
           of chosen item.
        """
        # see above here the helper function
        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence
        page.should_be_button_for_adding_to_basket()

        # check for button "Add to basket" clickability
        page.should_be_clickable_button_for_adding_to_basket()

        # check for success message after adding item to basket
        page.should_be_success_message_after_adding_to_basket()

        # check for adding item to basket with the same name
        page.should_be_correct_item_in_basket_after_adding()

        # check for adding item to basket with the same price
        page.should_be_correct_price_in_basket_after_adding()
