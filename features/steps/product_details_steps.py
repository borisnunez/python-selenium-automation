from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR,('a[aria-label*="Color"]'))
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-81970751 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/jockey-generation-men-s-cotton-stretch-crewneck-3pk-t-shirt/-/A-81970751?preselect=81838418#lnk=sametab')
    sleep(5)


@then('Verify user can click through different colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'White']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        # for visibility only:
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'