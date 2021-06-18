from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def generate_email(self):
        email = str(time.time()) + "@fakemail.org"
        return email

    def generate_password(self):
        password = str(time.time()) + "FakePwd"
        return password

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
