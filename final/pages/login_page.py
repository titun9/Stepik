from final.pages.base_page import BasePage
from final.pages.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def generate_email(self):
        email = str(time.time()) + "@fakemail.org"
        return email

    def generate_password(self):
        password = str(time.time()) + "FakePwd"
        return password

    def login_user(self, email, password):
        self.should_be_login_page()
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PWD_LOGIN).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN).click()

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_REGISTER).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PWD_REGISTER).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_PWD_CONFIRM_REGISTER).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_link = self.browser.current_url
        assert 'login' in current_link, "No page name in the link"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def user_should_be_logged_in(self):
        assert self.is_element_present(*LoginPageLocators.MESSAGE_SUCCESS), "Message success is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGOUT_LINK), "Logout link is not presented"

    def user_should_not_be_logged_in(self):
        assert self.is_element_present(*LoginPageLocators.MESSAGE_ERROR_LOGIN), "Message error is not presented"
        assert self.is_element_present(*LoginPageLocators.MESSAGE_HELP_LOGIN), "Message help is not presented"
        self.should_be_login_page()
