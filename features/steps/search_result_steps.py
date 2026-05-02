from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')



@then("Verify search results for {product} shown")
def verify_search_results(context, product):
    #actual_result = context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
    #assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'
    context.app.search_results_page.verify_search_results(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(0.5)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    # To scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", "")

    products = context.driver.find_elements(*LISTINGS)  # [WebEl1, ...etc]
    print(products)

    for product in products[:4]: #to only see the first 4 products
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f'*{title}')
        product.find_element(*PRODUCT_IMG)