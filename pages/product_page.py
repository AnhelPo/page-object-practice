"""
Class for product page.
"""

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_for_adding_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "BUTTON for ADD TO BASKET is missing!"

    def should_be_clickable_button_for_adding_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_success_message_after_adding_to_basket(self):
        message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE).text
        assert "has been added to your basket" in message,\
            "MESSAGE about successful adding item to basket IS MISSING!"

    def should_be_correct_item_in_basket_after_adding(self):
        item_name_should_be = self.browser.find_element(
             *ProductPageLocators.ITEM_NAME).text
        item_name_in_basket = self.browser.find_element(
             *ProductPageLocators.ITEM_NAME_IN_BASKET).text
        assert item_name_should_be == item_name_in_basket,\
            "Wrong ITEM in BASKET!"

    def should_be_correct_price_in_basket_after_adding(self):
        item_price_should_be = self.browser.find_element(
            *ProductPageLocators.ITEM_PRICE).text
        item_price_in_basket = self.browser.find_element(
            *ProductPageLocators.ITEM_PRICE_IN_BASKET).text
        assert item_price_should_be == item_price_in_basket,\
            "Wrong PRICE in BASKET!"

    def should_not_be_success_message_after_adding_item_to_basket(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEM_NAME_IN_BASKET),\
            "ITEM is in BASKET (and should be there)!"

    def should_not_be_success_message_before_adding_item_to_basket(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEM_NAME_IN_BASKET),\
            "ITEM is in BASKET (and should not be there)!"

    def should_message_disappear_after_adding_product_to_basket(self):
        assert self.is_disappeared(
            *ProductPageLocators.ITEM_NAME_IN_BASKET),\
            "ITEM does not disappear from BASKET (and should not)!"
