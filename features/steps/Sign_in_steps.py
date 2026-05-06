from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click on Sing in from right side navigation menu")
def click_on_singin(context):
    context.app.sign_in_page.sign_in()



@then('Verify Sing in form opened')
def verify_sing_in_form(context):
    context.app.sign_in_page.verify_sign_in()
