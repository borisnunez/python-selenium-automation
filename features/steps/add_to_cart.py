from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

#specific description of item added to cart
ADD_TO_CART_ICON = (By.CSS_SELECTOR, 'button[aria-label="Add Folgers Classic Medium Roast Ground Coffee - 25.9oz to cart"]')
ADD_TO_CART_AGAIN = (By.CSS_SELECTOR, 'button[aria-label="Add to cart for Folgers Classic Medium Roast Ground Coffee - 25.9oz"]')
PRODUCT_IN_CART = (By.XPATH, '//span[text()="Added to cart"]')

@when('Click "Add to Cart" for selected {search_query}')
def click_add_to_cart(context, search_query):
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_ICON), message= 'Add to Cart not visible').click()
    #alternative
    #context.driver.find_element(*ADD_TO_CART_ICON).click()
    #context.driver.find_elements(*ADD_TO_CART_ICON)[3].click()



@when('Click "Add to Cart" on side window for {search_query}')
def click_add_to_cart_again(context, search_query):
    #context.driver.find_element(*ADD_TO_CART_AGAIN).click()
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_AGAIN), message= 'Add to Cart not visible').click()


@then("Verify product added to cart")
def verify_product_in_cart(context):
    actual = context.driver.find_element(*PRODUCT_IN_CART).text
    expected = 'Added to cart'
    assert actual == expected, f'Expected {expected} did not match actual {actual}'
    sleep(1)