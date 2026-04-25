from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#specific description of item added to cart
ADD_TO_CART_ICON = (By.CSS_SELECTOR, 'button[aria-label="Add Franklin Sports Size 13 Youth Soccer Cleats: Kids Splatter Design, Lace Up, TPU Outsole to cart"]')
ADD_TO_CART_AGAIN = (By.CSS_SELECTOR, 'button[aria-label="Add to cart for Franklin Sports Size 13 Youth Soccer Cleats: Kids Splatter Design, Lace Up, TPU Outsole"]')
PRODUCT_IN_CART = (By.XPATH, '//span[text()="Added to cart"]')

@when('Click "Add to Cart" for selected {search_query}')
def click_add_to_cart(context, search_query):
    context.driver.find_element(*ADD_TO_CART_ICON).click()
    sleep(7)


@when('Click "Add to Cart" again for {search_query}')
def click_add_to_cart_again(context, search_query):
    context.driver.find_element(*ADD_TO_CART_AGAIN).click()
    sleep(7)


@then("Verify product added to cart")
def verify_product_in_cart(context):
    actual = context.driver.find_element(*PRODUCT_IN_CART).text
    expected = 'Added to cart'
    assert actual == expected, f'Expected {expected} did not match actual {actual}'
    sleep(3)