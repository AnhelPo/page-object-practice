'''
Test for product page.
Checks:
 - button for adding item to the shopping cart exists on page and is clickable,
 - after click on button for adding item to the cart:
        * alert messages are proseeded correctly and code is recieved,
        * the name of item in the cart matches the name of chosen item,
        * the price of item in the cart matches the price of chosen item.
'''

from pages.product_page import ProductPage

URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.should_be_clickable_button_for_adding_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_item_in_cart()
    page.should_be_correct_price_in_cart()
