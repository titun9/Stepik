import pytest
from final.pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/accounts/login/"
email = "ttitun9@mail.ru"
password = "BVDddJkDnTX46yD"


@pytest.mark.personal_tests
class TestLoginPage:
    def test_user_can_login_with_correct_credentials(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.login_user(email, password)

        # Assert
        page.user_should_be_logged_in()

    def test_user_cant_login_with_incorrect_password(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        generated_password = page.generate_password()
        page.login_user(email, generated_password)

        # Assert
        page.user_should_not_be_logged_in()

    def test_user_can_register(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.register_new_user(page.generate_email(), page.generate_password())

        # Assert
        page.user_should_be_logged_in()

    @pytest.mark.parametrize('incorrect_email',
                             ["@mail.ru", "new_user_123@mail.",
                              "new_user_123@.ru", "new_user_123mail.ru"])
    def test_user_cant_register_with_incorrect_email(self, browser, incorrect_email):
        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.register_new_user(incorrect_email, page.generate_password())

        # Assert
        page.should_be_login_page()
