from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10, name=None, price=None):
        super().__init__(browser, url, timeout)
        self.name = name
        self.price = price

    def get_book_name_and_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not presented"
        self.name = self.get_element_text(*ProductPageLocators.BOOK_NAME)
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is not presented"
        self.price = self.get_element_text(*ProductPageLocators.BOOK_PRICE)

    def add_product_to_card(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button not presented"
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def checking_the_name_and_price_of_the_added_product(self):
        assert self.is_element_present(*ProductPageLocators.ALERTINNER_BOOK_NAME), \
            "No messages about adding a product to the cart"
        assert self.name == self.browser.find_element(*ProductPageLocators.ALERTINNER_BOOK_NAME).text, \
            "Allert name does not match the product name"
        assert self.is_element_present(*ProductPageLocators.ALERTINNER_BOOK_PRICE), \
            "No messages about backet price"
        assert self.price == self.browser.find_element(*ProductPageLocators.ALERTINNER_BOOK_PRICE).text, \
            "Allert price does not match the product price"