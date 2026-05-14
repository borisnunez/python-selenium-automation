from behave import given, when, then
from time import sleep


@given('Open Sign in page')
def open_sign_in(context):
    context.app.target_app_page.open_sign_in()

@when('Click on Target terms and conditions link')
def click_on_terms_and_conditions_link(context):
    context.app.target_app_page.click_on_terms_and_conditions_link()
    # sleep(1)
    # print('All windows after clicking TC link', context.driver.window_handles)
    # print('Current window', context.app.page.get_current_window())

@then('Verify Terms and Conditions page is opened')
def verify_tc_page_opened(context):
    context.app.terms_and_conditions_page.verify_tc_page_opened()
