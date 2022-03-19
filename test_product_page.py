'''
Test for product page.
Checks:
 - button for adding item to the shopping cart exists on page and is clickable,
 - after click on button for adding item to the cart:
        * alert messages are proseeded correctly and code is recieved,
        * the name of item in the cart matches the name of chosen item,
        * the price of item in the cart matches the price of chosen item.
'''

import pytest

from pages.product_page import ProductPage

LINKS = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

LINKS[7] = pytest.param(LINKS[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize("link", LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_clickable_button_for_adding_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_item_in_cart()
    page.should_be_correct_price_in_cart()
