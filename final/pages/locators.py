from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INPUT_SEARCH = (By.CSS_SELECTOR, "[type='search']")
    BUTTON_SEARCH = (By.CSS_SELECTOR, ".btn[value='Search']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_REGISTER = (By.CSS_SELECTOR, "[name='registration-email']")
    INPUT_PWD_REGISTER = (By.CSS_SELECTOR, "[name='registration-password1']")
    INPUT_PWD_CONFIRM_REGISTER = (By.CSS_SELECTOR, "[name='registration-password2']")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[name='registration_submit']")
    INPUT_EMAIL_LOGIN = (By.CSS_SELECTOR, "[name='login-username']")
    INPUT_PWD_LOGIN = (By.CSS_SELECTOR, "[name='login-password']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "[name='login_submit']")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    LOGOUT_LINK = (By.CSS_SELECTOR, "[id='logout_link']")
    MESSAGE_ERROR_LOGIN = (By.CSS_SELECTOR, ".login_form .alert-danger:nth-of-type(1)")
    MESSAGE_HELP_LOGIN = (By.CSS_SELECTOR, ".login_form .alert-danger:nth-of-type(2)")


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
    BUTTON_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn")
    LANGUAGE_PAGE = (By.TAG_NAME, "html")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    TABLE_ADDED_PRODUCT = (By.CSS_SELECTOR, ".basket_summary")
    TITLE_PAGE_BASKET = (By.CSS_SELECTOR, ".page-header h1")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")


class SearchPageLocators():
    MESSAGE_FOUND_REQUEST = (By.CSS_SELECTOR, ".page-header.action")
    SORT = (By.CSS_SELECTOR, "[name='sort_by']")
    FOUND_PRODUCT = (By.CSS_SELECTOR, "li:nth-child(1) .product_pod")
