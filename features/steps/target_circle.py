from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TARGET_CIRCLE = (By.ID, 'utilityNav-circle')
STORYCARD_1 = (By.CSS_SELECTOR, 'a[data-lnk*="C_TargetCircle360™"]')
STORYCARD_2 = (By.CSS_SELECTOR, 'img[alt*="Explore Target Circle™ Card"]')
@when('Click on Target Circle')
def click_target_circle(context):
    context.driver.find_element(*TARGET_CIRCLE).click()
    sleep(3)

@then("Verify {expected_amount} storycards are shown")
def verify_storycard_amount(context, expected_amount):  #  expected_amount = " "
    expected_amount = int(expected_amount)# expected_amount "2" => 2 "integer"
    storycard1 = context.driver.find_elements(*STORYCARD_1)
    storycard2 = context.driver.find_element(*STORYCARD_2)
    storycards = [storycard1, storycard2]
    print('\nCircle storycards: ')
    print(storycards)
    # assert 2 storycards are shown
    assert len(storycards) == expected_amount, f'Expected {expected_amount} stoycards but got {len(storycards)}'



