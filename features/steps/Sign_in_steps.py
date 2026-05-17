from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click on Sing in from right side navigation menu")
def click_on_signin(context):
    context.app.sign_in_page.sign_in()


@then('Verify Sing in form opened')
def verify_sing_in_form(context):
    context.app.sign_in_page.verify_sign_in()


@when('Enter correct email "{email}" and click continue')
def enter_email(context, email):
    #context.wait.until(EC.element_to_be_clickable(SEARCH_FIELD), message= ' Search field not visible').send_keys(search_query)
    #context.wait.until(EC.element_to_be_clickable(SEARCH_BTN), message='Search button not visible').click()
    #sleep(1)
    context.app.sign_in_page.enter_email(email)


@when('Enter incorrect password "{password}"')
def enter_password(context, password):
    context.app.sign_in_page.enter_password(password)


@then('Verify that en error message is shown')
def verify_error_message(context):
    context.app.sign_in_page.verify_error_message()