from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)

@when("Click on cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[class*="styles_cartIconDiv"]').click()
    sleep(2)

@when("Click on Sing in")
def click_on_singin(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span[class*="sc-40e81479-3"]').click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()
    sleep(2)

@then('Should see "Your cart is empty" message')
def verify_cart_empty(context):
    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1[class*=styles_ndsHeading]").text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'

@then('Verify Sing in form opened')
def verify_sing_in_form(context):
    expected_result = "Sign in or create account"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1[class*="styles_ndsHeading"]').text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'
