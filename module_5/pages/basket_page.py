from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def get_correct_message_empty_basket(self):
        language = self.browser.find_element(*BasePageLocators.LANGUAGE_PAGE).get_attribute("lang")
        dictionary_message = {"ru": "Ваша корзина пуста", "en-gb": "Your basket is empty", \
                              "es": "Tu carrito esta vacío", "fr": "Votre panier est vide"}
        message = dictionary_message[language]
        return message

    def should_be_message_empty_basket(self):
        message = self.get_correct_message_empty_basket()
        message_basket_empty = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        assert message in message_basket_empty, f"No message that basket is empty"

    def should_be_product_in_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.TABLE_ADDED_PRODUCT), \
            "Basket is not empty"

    def should_not_be_product_in_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.TABLE_ADDED_PRODUCT), \
            "Basket is empty"
