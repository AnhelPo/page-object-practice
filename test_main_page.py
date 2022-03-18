'''
Tests for the main page.
Checks out:
    - guest user can go to login page from the main page.
'''

from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    LINK = "http://selenium1py.pythonanywhere.com/"
    browser.get(LINK)
    login_link = browser.find_element(By.ID, "login_link")
    login_link.click()
