from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):

    CLICK_ON_SIGNIN = (By.XPATH, "//button[text()='Sign in or create account']")
    SIGN_IN_SIDE_WDW = (By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]')
    VERIFY_SIGN_IN = (By.CSS_SELECTOR, 'h1[class*="styles_ndsHeading"]')
    ENTER_USERNAME_FIELD = (By.CSS_SELECTOR, 'input[id="username"]')
    CONTINUE = (By.CSS_SELECTOR, 'button[id="login"]')
    ENTER_PASSWORD_OPTION = (By.XPATH, "//span[text()='Enter your password']")
    ENTER_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="password"]')
    SIGN_IN_WITH_PASSWORD = (By.XPATH, "//button[text()='Sign in with password']")
    VERIFY_ERROR_MSG = (By.XPATH, "//div[text()='That password is incorrect. Please try again.']")

    def sign_in(self):
        self.find_element(*self.CLICK_ON_SIGNIN).click()
        ##self.find_element(*self.SIGN_IN_SIDE_WDW).click()

    def verify_sign_in(self):
        expected_result = "Sign in or create account"
        actual_result = self.find_element(*self.VERIFY_SIGN_IN).text
        assert expected_result in actual_result, f"Expected \"{expected_result}\" not in actual \"{actual_result}\" "

    def enter_email(self, email: str):
        self.input_text(email, *self.ENTER_USERNAME_FIELD)
        self.click(*self.CONTINUE)
        #sleep(10)

    def enter_password(self, password: str):
        self.click(*self.ENTER_PASSWORD_OPTION)
        self.input_text(password, *self.ENTER_PASSWORD_FIELD)
        self.click(*self.SIGN_IN_WITH_PASSWORD)
        sleep(2)

    def verify_error_message(self):
        expected_result = "That password is incorrect. Please try again."
        actual_result = self.find_element(*self.VERIFY_ERROR_MSG).text
        assert expected_result in actual_result, f"Expected \"{expected_result}\" not in actual \"{actual_result}\" "
