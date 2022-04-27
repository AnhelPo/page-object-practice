"""
Class for basket page.
"""

from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_is_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS),\
            "BASKET is NOT EMPTY!"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.IS_EMPTY_MESSAGE),\
            "'Your basket is empty' MESSAGE is MISSING!"
