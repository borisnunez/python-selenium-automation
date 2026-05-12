from behave import given, when, then
from time import sleep


@given('Open Sign in page')
def open_sign_in(context):
    context.app.target_app_page.open_sign_in()

@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window', context.original_window)
    print('All windows', context.driver.window_handles)

@when('Click on Target terms and conditions link')
def click_on_terms_and_conditions_link(context):
    context.app.target_app_page.click_on_terms_and_conditions_link()
    sleep(1)
    print('All windows after clicking TC link', context.driver.window_handles)
    print('Current window', context.app.page.get_current_window())

@when('Switch to new window')
def switch_window(context):
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])
    print('Current window after switch', context.app.page.get_current_window())

@then('Verify Terms and Conditions page is opened')
def verify_tc_page_opened(context):
    context.app.terms_and_conditions_page.verify_tc_page_opened()

@then('User can close new window')
def close_new_window(context):
    context.app.page.close()
    print('All closed windows after TC', context.driver.window_handles)

@then('Switch back to original')
def switch_to_original_window(context):
    context.app.page.switch_to_window_by_id(context.original_window)
    print('Current window after switch', context.app.page.get_current_window())