'''
Class for product page.
'''

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_clickable_button_for_adding_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), \
                    "BUTTON for ADD TO CART is missing!"
        add_to_cart_button = self.browser.find_element(
                                         *ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_correct_item_in_cart(self):
        assert self.is_element_present(
                                        *ProductPageLocators.ITEM_NAME_IN_CART), \
                    "ITEM was not added to CART!"
        item_name_should_be = self.browser.find_element(
                                        *ProductPageLocators.ITEM_NAME).text
        item_name_in_cart = self.browser.find_element(
                                        *ProductPageLocators.ITEM_NAME_IN_CART).text
        assert item_name_should_be == item_name_in_cart, \
                    "Wrong ITEM in CART!"

    def should_be_correct_price_in_cart(self):
        item_price_should_be = self.browser.find_element(
                                        *ProductPageLocators.ITEM_PRICE).text
        item_price_in_cart = self.browser.find_element(
                                        *ProductPageLocators.ITEM_PRICE_IN_CART).text
        assert item_price_should_be == item_price_in_cart, \
                    "Wrong PRICE in CART!"
