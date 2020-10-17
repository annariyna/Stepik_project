from .pages.main_page import MainPage
import pytest
from selenium import webdriver

class TestMainPage:

    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

    def test_search_item(self, browser):
        search_text = "Coders at Work"

        main_page = MainPage(browser)
        main_page.open()
        main_page.search_item(search_text)