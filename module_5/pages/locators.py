from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_GALLERY = (By.CSS_SELECTOR, "#product_gallery")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    TITLE_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    TITLE_PRODUCT_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_PRODUCT_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
