from final.pages.base_page import BasePage
from final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()

    def should_be_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button basket is not presented"

    def should_be_message_with_title_product(self):
        title_product = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT).text
        title_product_alert = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT_ALERT).text
        assert title_product == title_product_alert, \
            f"Incorrect title of product of alert. \
             Expected title - {title_product}, Actual title - {title_product_alert}"

    def should_be_message_with_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_product_alert = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ALERT).text
        assert price_product == price_product_alert, \
            f"Incorrect price of product of alert. \
             Expected price - {price_product}, Actual price - {price_product_alert}"

    def should_be_product_gallery(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_GALLERY), "Product gallery is not presented"

    def should_be_product_page(self):
        self.should_be_product_gallery()
        self.should_be_button_basket()

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
