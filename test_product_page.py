from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import time


def test_find_name_and_price(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.get_book_name_and_price()
    page.add_product_to_card()
    page.checking_the_name_and_price_of_the_added_product()
    time.sleep(5)