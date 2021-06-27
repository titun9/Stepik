import pytest
from final.pages.main_page import MainPage
from final.pages.login_page import LoginPage
from final.pages.basket_page import BasketPage
from final.pages.search_page import SearchPage

link = "http://selenium1py.pythonanywhere.com/"
name_product_search = "art"


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


@pytest.mark.personal_tests
class TestSearchProductPage():
    def test_guest_can_search_existing_product(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.search_product(name_product_search)
        search_page = SearchPage(browser, browser.current_url)

        # Assert
        search_page.should_be_search_page_with_product()

    def test_guest_cant_search_nonexistent_product(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.search_product(page.generate_string())
        search_page = SearchPage(browser, browser.current_url)

        # Assert
        search_page.should_be_search_page_with_no_product()
