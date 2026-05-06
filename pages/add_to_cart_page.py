from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class AddToCartPage(Page):

    ADD_TO_CART_ICON = (By.CSS_SELECTOR, 'button[aria-label="Add Folgers Classic Medium Roast Ground Coffee - 25.9oz to cart"]')
    ADD_TO_CART_AGAIN = (By.CSS_SELECTOR, 'button[aria-label="Add to cart for Folgers Classic Medium Roast Ground Coffee - 25.9oz"]')
    PRODUCT_IN_CART = (By.XPATH, '//span[text()="Added to cart"]')

    def add_to_cart(self):
        self.find_element(*self.ADD_TO_CART_ICON).click()


    def add_to_cart_again(self):
        self.find_element(*self.ADD_TO_CART_AGAIN).click()


    def add_to_cart_verify(self):
        actual = self.find_element(*self.PRODUCT_IN_CART).text
        expected = 'Added to cart'
        assert actual == expected, f'Expected {expected} did not match actual {actual}'
        sleep(1)