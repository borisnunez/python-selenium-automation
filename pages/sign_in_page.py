from selenium.webdriver.common.by import By
from pages.base_page import Page



class SignInPage(Page):

    CLICK_ON_SIGNIN = (By.CSS_SELECTOR, 'span[class*="sc-40e81479-3"]')
    SIGN_IN_SIDE_WDW = (By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]')
    VERIFY_SIGN_IN = (By.CSS_SELECTOR, 'h1[class*="styles_ndsHeading"]')

    def sign_in(self):
        self.find_element(*self.CLICK_ON_SIGNIN).click()
        self.find_element(*self.SIGN_IN_SIDE_WDW).click()


    def verify_sign_in(self):
        expected_result = "Sign in or create account"
        actual_result = self.find_element(*self.VERIFY_SIGN_IN).text
        assert expected_result in actual_result, f"Expected \"{expected_result}\" not in actual \"{actual_result}\" "

