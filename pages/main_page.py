from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    main_page_link = "http://selenium1py.pythonanywhere.com"

    def __init__(self,browser):
        BasePage.__init__(self,browser,MainPage.main_page_link)

    def search_item(self,search_text):
        search = self.find(MainPageLocators.search_input_locator)
        search.send_keys(search_text)
        button = self.find(MainPageLocators.search_submit)
        button.click()

        result = self.find(MainPageLocators.search_title_locator)

        assert search_text in result.text, \
            "Search page title '%s' should contain search text '%s'" % (result.text, search_text)

        return result.text

