'''
Contains locators for all elements in project.
'''

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_invalid")


class MainPageLocators:
    pass


class LoginPageLocators:
    EMAIL_LOGIN = (By.ID, "id_login-username")
    PASSWORD_LOGIN = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    EMAIL_REGISTER = (By.ID, "id_registration-email")
    PASSWORD1_REGISTER = (By.ID, "id_registration-password1")
    PASSWORD2_REGISTER = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR,
                    "[name='registration_submit']")


class ProductPageLocators:
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME_IN_CART = (By.CSS_SELECTOR,
                    "#messages .alert:nth-of-type(1) .alertinner strong")
    ITEM_PRICE_IN_CART = (By.CSS_SELECTOR,
                    "#messages .alert:nth-of-type(3) .alertinner p strong")
