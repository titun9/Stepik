from final.pages.locators import MainPageLocators
from final.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def search_product(self, name_product):
        self.browser.find_element(*MainPageLocators.INPUT_SEARCH).send_keys(name_product)
        self.browser.find_element(*MainPageLocators.BUTTON_SEARCH).click()
