from selenium.webdriver.common.by import By
from behave import given, when, then

#specific description of item added to cart
ADD_TO_CART_ICON = (By.CSS_SELECTOR, 'button[aria-label="Add Folgers Classic Medium Roast Ground Coffee - 25.9oz to cart"]')
ADD_TO_CART_AGAIN = (By.CSS_SELECTOR, 'button[aria-label="Add to cart for Folgers Classic Medium Roast Ground Coffee - 25.9oz"]')
PRODUCT_IN_CART = (By.XPATH, '//span[text()="Added to cart"]')

@when('Click "Add to Cart" for selected {search_query}')
def click_add_to_cart(context, search_query):
    context.app.add_to_cart_page.add_to_cart()


@when('Click "Add to Cart" on side window for {search_query}')
def click_add_to_cart_again(context, search_query):
    context.app.add_to_cart_page.add_to_cart_again()


@then("Verify product added to cart")
def verify_product_in_cart(context):
    context.app.add_to_cart_page.add_to_cart_verify()