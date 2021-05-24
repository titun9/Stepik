from selenium import webdriver

# Links
link_login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

# Data of user
email = "ttitun9@mail.ru"
password = "BVDddJkDnTX46yD"

# Locators
input_email_locator = "input[name='login-username']"
input_password_locator = "input[name='login-password']"
button_login_locator = "button[name='login_submit']"
logout_link_locator = "a[id='logout_link']"
account_link_locator = ".navbar-right li:nth-child(1) a"
welcome_message_locator = ".alertinner.wicon"


def test_login_user():
    # Data
    welcome_message = "Рады видеть вас снова"
    name_logout_link = "Logout"
    name_account_link = "Account"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link_login_page)

        input_email = browser.find_element_by_css_selector(input_email_locator)
        input_password = browser.find_element_by_css_selector(input_password_locator)
        button_login = browser.find_element_by_css_selector(button_login_locator)

        # Act
        input_email.send_keys(email)
        input_password.send_keys(password)
        button_login.click()

        # Assert
        welcome_message_text = browser.find_element_by_css_selector(welcome_message_locator).text
        assert welcome_message == welcome_message_text, \
            f"Ожидается приветственное сообщение '{welcome_message}', а получено '{welcome_message_text}'"
        logout_link_text = browser.find_element_by_css_selector(logout_link_locator).text
        assert name_logout_link == logout_link_text, \
            f"Ожидается название кнопки выхода из аккаунта '{name_logout_link}', а получено '{logout_link_text}'"
        account_link_text = browser.find_element_by_css_selector(account_link_locator).text
        assert name_account_link == account_link_text, \
            f"Ожидается название кнопки аккаунта '{name_account_link}', а получено '{account_link_text}'"

    finally:
        browser.quit()


test_login_user()
