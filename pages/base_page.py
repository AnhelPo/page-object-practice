"""
Base class for all pages in project.

!! Method for stepik quiz was removed as redundant.
!! Methods are intentionally grouped by theme, not in alphabetical order.
"""


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from pages.locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK),\
            "LOGIN link is MISSING!"

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(
            *BasePageLocators.VIEW_BASKET_LINK),\
            "BASKET link is MISSING!"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(
            *BasePageLocators.VIEW_BASKET_LINK)
        basket_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON),\
            "USER ICON is MISSING, probably unauthorized user!"
