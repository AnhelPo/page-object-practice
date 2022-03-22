'''
Tests for the main page.
Checks:
 - login link exists,
 - guest user can go to the login page from the main page,
 - login page has correct URL and contains correct forms for
   log in and registration,
 - basket link exists,
 - guest user can go to the basket page from the main page,
 - if no item was added to cart, the cart is empty and a message
   about empty cart is shown.
'''

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

URL = "http://selenium1py.pythonanywhere.com/"


def get_class_instance_and_open_page(browser):
    '''Precondition for all tests. Function is called from tests.'''

    page = MainPage(browser, URL)
    page.open()
    return page


def test_guest_can_go_to_login_page_from_main_page(browser):
    '''Guest can see login link on the main page and can go to
    the login page from the main page.'''

    main_page = get_class_instance_and_open_page(browser)

    # check for login link existence on the main page; BasePage method
    main_page.should_be_login_link()

    # go to the login page; BasePage method
    main_page.go_to_login_page()

    # browser.current_url has changed to login page URL
    login_page = LoginPage(browser, browser.current_url)

    # check for correct URL and forms for log in and registration
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    '''Guest can see basket link on the main page and can go to basket page.
    If no item was added to cart, the cart on basket page is empty and
    a message about an empty cart is shown.
    '''

    main_page = get_class_instance_and_open_page(browser)

    # check for basket link existence on the main page; BasePage method
    main_page.should_be_basket_link()

    # go to the basket page; BasePage method
    main_page.go_to_basket_page()

    # browser.current_url has changed to basket page URL
    basket_page = BasketPage(browser, browser.current_url)

    # check for no items in cart
    basket_page.should_not_be_items_is_cart()

    # check for message "Your basket is empty"
    basket_page.should_be_message_about_empty_basket()
