from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
    #FAV_ICON = ()
    #FAV_TOOLTIP = ()

    #def hover_fav_icon(self):
      #  fav_icon = self.find_element(*self.FAV_ICON)
       # actions = ActionChains(self.driver)
        #actions.move_to_element()
        #actions.perform()

    #def verify_fav_tooltip(self):
     #   pass


    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULT_COUNT_TEXT).text
        assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'
