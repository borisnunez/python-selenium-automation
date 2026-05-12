from selenium.webdriver.common.by import By
from pages.base_page import Page


class TargetAppPage(Page):

    TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR, 'a[aria-label*="terms & conditions"]')

    def open_sign_in(self):
        self.open_url(end_url='orders?lnk=acct_nav_my_account')

    def click_on_terms_and_conditions_link(self):
        self.click(*self.TERMS_AND_CONDITIONS_LINK)

