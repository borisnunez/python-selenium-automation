from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page



class HelpPage(Page):

    SELECT_TOPIC_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTR}']") #Dynamic Locator

    def get_header_locator(self, expected_text):
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTR}', expected_text)]

    def open_help_returns(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, topic):
        dropdown = self.find_element(*self.SELECT_TOPIC_DD)
        select = Select(dropdown)
        select.select_by_value(topic)

    def verify_header_present(self, expected_text):
        locator = self.get_header_locator(expected_text)
        self.wait_until_appear(*locator)

