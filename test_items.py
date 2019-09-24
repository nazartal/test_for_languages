from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def basket_button_present(browser):
    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except (NoSuchElementException):
        return False
    return True

def test_add_in_basket_button(browser):
    browser.get(link)
    assert add_in_basket_button_present(browser), "Кнопка добавления в корзину не найдена"
    time.sleep(30)
