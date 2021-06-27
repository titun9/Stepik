from final.pages.base_page import BasePage
from final.pages.locators import SearchPageLocators


class SearchPage(BasePage):
    def go_to_product_page(self):
        self.browser.find_element(*SearchPageLocators.FOUND_PRODUCT).click()

    def should_be_search_page_with_product(self):
        self.should_be_message_found_request()
        self.should_be_sort()
        self.should_be_found_product()

    def should_be_search_page_with_no_product(self):
        self.should_be_message_found_request()
        self.should_not_be_sort()
        self.should_not_be_found_product()

    def should_be_message_found_request(self):
        assert self.is_element_present(*SearchPageLocators.MESSAGE_FOUND_REQUEST), \
            'Message found request is not presented'

    def should_be_sort(self):
        assert self.is_element_present(*SearchPageLocators.SORT), "Sort is not presented"

    def should_be_found_product(self):
        assert self.is_element_present(*SearchPageLocators.FOUND_PRODUCT), "Found product is not presented"

    def should_not_be_sort(self):
        assert self.is_not_element_present(*SearchPageLocators.SORT), "Sort is presented"

    def should_not_be_found_product(self):
        assert self.is_not_element_present(*SearchPageLocators.FOUND_PRODUCT), "Found product is presented"
