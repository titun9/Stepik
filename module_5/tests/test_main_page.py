from module_5.pages.main_page import MainPage
from module_5.pages.login_page import LoginPage
from module_5.pages.basket_page import BasketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"


class TestBasketFromMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = BasketPage(browser, link)
        page.open()

        # Act
        page.open_basket()

        # Assert
        page.should_not_be_product_in_basket_page()
        page.should_be_message_empty_basket()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Assert
        page.should_be_login_link()
