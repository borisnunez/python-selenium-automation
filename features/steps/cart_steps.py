from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_msg(context):
    actual = context.wait.until(EC.visibility_of_element_located(CART_EMPTY_MSG), message= 'Your Cart is empty msg not visible').text
    expected = 'Your cart is empty'
    assert actual == expected, f'Expected {expected} did not match actual {actual}'




