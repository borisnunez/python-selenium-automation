from pages.add_to_cart_page import AddToCartPage
from pages.base_page import Page
from pages.header_page import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import Cart
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.header_page = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = Cart(driver)
        self.sign_in_page = SignInPage(driver)
        self.add_to_cart_page = AddToCartPage(driver)