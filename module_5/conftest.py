import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB')
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


def language(request):
    get_language = request.config.getoption("language")
    print(get_language)
    list_language = ["ru", "en-GB", "es", "fr"]
    if get_language in list_language:
        return get_language
    else:
        raise pytest.UsageError(f"--Online store doesn't supported language {get_language}")


@pytest.fixture(scope="function")
def button_cart_name_dictionary(request):
    dictionary_cart_name = {"ru": "Добавить в корзину", "en-GB": "Add to basket", \
                            "es": "Añadir al carrito", "fr": "Ajouter au panier"}
    button_name = dictionary_cart_name[language(request)]
    return button_name


@pytest.fixture(scope="function")
def browser(request):
    add_options = Options()
    get_language = language(request)
    prefs = {'intl.accept_languages': get_language}
    add_options.add_experimental_option("prefs", prefs)
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(options=add_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(options=add_options)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.save_screenshot('module_5/Screenshots/screenshot-%s.png' % now)
    driver.quit()
