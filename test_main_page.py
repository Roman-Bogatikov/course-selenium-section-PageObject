import time

import pytest

from pages.main_page import MainPage
from pages.basket_page import BasketPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(page.browser, page.url)
    basket_page.should_not_to_be_items_into_basket()
    basket_page.should_be_empty_basket_text()
