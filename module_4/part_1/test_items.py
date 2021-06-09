from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# Links
link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Locators
button_cart_locator = ".btn-add-to-basket"


def test_button_basket(browser, button_cart_name_dictionary):
    # Arrange
    browser.get(link_product_page)

    # Act
    actual_name_button_cart = browser.find_element_by_css_selector(button_cart_locator).get_attribute('value')

    # Assert
    assert actual_name_button_cart == button_cart_name_dictionary, \
        f"Ожидаемое название кнопки - {button_cart_name_dictionary}, фактическое название - {actual_name_button_cart}"
