from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("Click on Sing in")
def click_on_singin(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span[class*="sc-40e81479-3"]').click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()
    sleep(2)


@then('Verify Sing in form opened')
def verify_sing_in_form(context):
    expected_result = "Sign in or create account"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1[class*="styles_ndsHeading"]').text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'
