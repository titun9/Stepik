from module_5.pages.product_page import ProductPage
import pytest
from module_5.pages.login_page import LoginPage
from module_5.pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        url = link + '?promo=' + promo_offer
        page = ProductPage(browser, url)
        page.open()

        # Assert
        page.should_be_product_page()

        # Act
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_be_message_with_title_product()
        page.should_be_message_with_price_product()

    @pytest.mark.xfail(reason="expected bug")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="expected bug")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.open_basket()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_not_be_product_in_basket_page()
        basket_page.should_be_message_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        url = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, url)
        page.open()
        page.register_new_user(page.generate_email(), page.generate_password())
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_be_product_page()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_be_message_with_title_product()
        page.should_be_message_with_price_product()

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_not_be_success_message()
