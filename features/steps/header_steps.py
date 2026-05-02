from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
VERIFY_HEADER_LINKS = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")
VERIFY_HEADER_LINKS_AMT = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")

@when('Click on Cart icon')
def click_cart(context):
    #context.driver.find_element(*CART_ICON).click()
    #context.wait.until(EC.element_to_be_clickable(CART_ICON), message='Cart icon not visible').click()
    context.app.header.click_on_cart()

@when("Search for {search_query}")
def search_product(context, search_query):
    #context.wait.until(EC.element_to_be_clickable(SEARCH_FIELD), message= ' Search field not visible').send_keys(search_query)
    #context.wait.until(EC.element_to_be_clickable(SEARCH_BTN), message='Search button not visible').click()
    #sleep(1)
    context.app.header.search_product(search_query)

@then("Verify header link container is shown")
def verify_header_links(context):
    e = context.driver.find_element(*VERIFY_HEADER_LINKS)
    print('\nHeader links container: ')
    print(e)


@then("Verify {expected_amount} links are shown")
def verify_header_link_amount(context, expected_amount):  #  expected_amount = "6"
    expected_amount = int(expected_amount) # expected_amount "6" => 6 "integer"
    links = context.driver.find_elements(*VERIFY_HEADER_LINKS_AMT)
    print('\nHeader links: ')
    print(links)
    # assert 6 == 6
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'



