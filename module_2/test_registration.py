from selenium import webdriver
from sys import argv

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element_by_css_selector(".first_block input.first")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_css_selector(".first_block input.second")
    input_last_name.send_keys("Fedorov")
    input_email = browser.find_element_by_css_selector(".first_block input.third")
    input_email.send_keys("ivan-ivan@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
