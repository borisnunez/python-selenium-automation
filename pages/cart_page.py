from selenium.webdriver.common.by import By
from pages.base_page import Page

class Cart(Page):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def cart_is_empty(self):
        actual = self.driver.find_element(*self.CART_EMPTY_MSG).text
        expected = 'Your cart is empty'
        assert actual == expected, f'Expected {expected} did not match actual {actual}'


