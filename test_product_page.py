'''
Tests for product page.
Checks:
 - button for adding item to the shopping cart exists on page and is clickable,
 - after click on button for adding item to the cart:
        * alert messages are handled correctly and code is recieved,
        * the name of item in the cart matches the name of chosen item,
        * the price of item in the cart matches the price of chosen item,
        * after adding item to cart success messages appear as expected,
 - login link exists on product page,
 - guest user can go to the login page from the product page,
 - login page has correct URL and contains correct forms for
   log in and registration,
 - basket link exists on product page,
 - guest user can go to the basket page from the product page,
 - if no item was added to cart by guest, the cart is empty and a message
   about empty cart is shown,
 - registered user can go to the basket page from the product page,
 - if no item was added to cart by registered user, the cart is empty
   and a message about empty cart is shown.
'''

import time
import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def get_class_instance_and_open_page(browser):
    '''Precondition for all tests. Is called from tests.'''

    page = ProductPage(browser, URL)
    page.open()
    return page


def generate_email_and_password():
    '''Prepares data for registration of a new user.'''

    email = str(time.time())[-10:] + "@fakemail.org"
    password = str(time.time())[-10:]
    return email, password


@pytest.mark.login_from_product_page
class TestLoginFromProductPage:

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        '''Guest can see login link on the product page and can go to
        the login page from the product page.
        '''

        product_page = get_class_instance_and_open_page(browser)

        # check for login link existance; BasePage method
        product_page.should_be_login_link()

        # check for login link clickability; BasePage method
        product_page.go_to_login_page()

        # browser.current_url has changed to login page URL
        login_page = LoginPage(browser, browser.current_url)

        # check for correct URL and forms for log in and registration
        login_page.should_be_login_page()


@pytest.mark.guest_add_to_basket
class TestGuestAddToBasketFromProductPage:

    def test_guest_can_add_product_to_basket(self, browser):
        '''Guest can see button for adding to cart and can click on it.
        Item should be added to cart. Item's name and price in cart
        matches chosen one.
        '''

        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence and clickability
        page.should_be_clickable_button_for_adding_to_cart()

        # check for successful adding item to cart
        # and check for item's name in cart
        page.should_be_correct_item_in_cart_after_adding()

        # check for item's price in cart
        page.should_be_correct_price_in_cart_after_adding()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        '''No message is shown to guest after adding item to cart.'''

        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence and clickability
        page.should_be_clickable_button_for_adding_to_cart()

        # check for no message is shown
        page.should_not_be_success_message_after_adding_item_to_cart()

    def test_guest_cant_see_success_message(self, browser):
        '''No message is shown before adding item to cart.'''

        page = get_class_instance_and_open_page(browser)

        # check for no message is shown
        page.should_not_be_success_message_before_adding_item_to_cart()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        '''Message about successful adding item to cart disappeares.'''

        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence and clickability
        page.should_be_clickable_button_for_adding_to_cart()

        # check for message disappearance
        page.should_message_disappear_after_adding_product_to_cart()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        '''Guest can see basket link on the product page and can go
        to basket page. If no item was added to cart, the cart on basket
        page is empty and a message about an empty cart is shown.
        '''

        product_page = get_class_instance_and_open_page(browser)

        # check for basket link existence on the main page; BasePage method
        product_page.should_be_basket_link()

        # go to the basket page; BasePage method
        product_page.go_to_basket_page()

        # browser.current_url has changed to basket page URL
        basket_page = BasketPage(browser, browser.current_url)

        # check for no items in cart
        basket_page.should_not_be_items_is_cart()

        # check for message "Your basket is empty"
        basket_page.should_be_message_about_empty_basket()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        '''From the product page guest goes to the login page and
        register as a new user. Log in as a new user is checked.
        '''

        product_page = get_class_instance_and_open_page(browser)

        # check for login link clickability; BasePage method
        product_page.go_to_login_page()

        # browser.current_url has changed to login page URL
        login_page = LoginPage(browser, browser.current_url)

        # generate data
        email, password = generate_email_and_password()

        # guest registrates with data as a new user
        login_page.register_new_user(email, password)

        # check the appearence of the user icon
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        '''No message is shown before adding item to cart.'''

        page = get_class_instance_and_open_page(browser)

        # check for no message is shown
        page.should_not_be_success_message_before_adding_item_to_cart()

    def test_user_can_add_product_to_basket(self, browser):
        '''User can see button for adding to cart and can click on it.
        Item should be added to cart. Item's name and price in cart
        matches chosen one.
        '''

        page = get_class_instance_and_open_page(browser)

        # check for button "Add to basket" existence and clickability
        page.should_be_clickable_button_for_adding_to_cart()

        # check for successful adding item to cart
        # and check for item's name in cart
        page.should_be_correct_item_in_cart_after_adding()

        # check for item's price in cart
        page.should_be_correct_price_in_cart_after_adding()
