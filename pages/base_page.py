class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find(self, locator):
        return self.browser.find_element_by_css_selector(locator)

    def find_all(self, locator):
        return self.browser.find_element_by_css_selector(locator)




