'''
Test for product page.
Checks:
 - button for adding item to the shopping cart exists on page and is clickable,
 - after click on button for adding item to the cart:
        * alert messages are proseeded correctly and code is recieved,
        * the name of item in the cart matches the name of chosen item,
        * the price of item in the cart matches the price of chosen item,
        * after adding item to cart success messages appear as expected.
'''

import pytest

from pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


# precondition for tests; is called from all tests
def get_class_instance_and_open_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    return page


def test_guest_can_add_product_to_basket(browser):
    page = get_class_instance_and_open_page(browser)
    page.should_be_clickable_button_for_adding_to_cart()
    page.should_be_correct_item_in_cart_after_adding()
    page.should_be_correct_price_in_cart_after_adding()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = get_class_instance_and_open_page(browser)
    page.should_be_clickable_button_for_adding_to_cart()
    page.should_not_be_success_message_after_adding_item_to_cart()


def test_guest_cant_see_success_message(browser):
    page = get_class_instance_and_open_page(browser)
    page.should_not_be_success_message_before_adding_item_to_cart()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = get_class_instance_and_open_page(browser)
    page.should_be_clickable_button_for_adding_to_cart()
    page.should_message_disappear_after_adding_product_to_cart()


def test_guest_should_see_login_link_on_product_page(browser):
    page = get_class_instance_and_open_page(browser)
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = get_class_instance_and_open_page(browser)
    page.go_to_login_page()
