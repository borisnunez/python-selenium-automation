from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CLICK_ON_SIGNIN = (By.CSS_SELECTOR, 'span[class*="sc-40e81479-3"]')
SIGN_IN_SIDE_WDW = (By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]')

@when("Click on Sing in")
def click_on_singin(context):
    context.wait.until(EC.element_to_be_clickable(CLICK_ON_SIGNIN), message= 'Sign in button not visible').click()
    context.wait.until(EC.element_to_be_clickable(SIGN_IN_SIDE_WDW), message= 'Side window Sign in button not visible').click()



@then('Verify Sing in form opened')
def verify_sing_in_form(context):
    expected_result = "Sign in or create account"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1[class*="styles_ndsHeading"]').text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'
