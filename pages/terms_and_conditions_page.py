from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsAndConditions(Page):

    def verify_tc_page_opened(self):
        self.wait_until_url_contains('terms-conditions')



