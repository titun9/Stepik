from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


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
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, welcome_message_locator)),
            message="Не отображается приветственное сообщение"
        )
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, logout_link_locator)),
            message="Не отображается кнопка выхода из аккаунта пользователя"
        )
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, account_link_locator)),
            message="Не отображается кнопка перехода в аккаунт пользователя"
        )

    finally:
        browser.quit()


test_login_user()
