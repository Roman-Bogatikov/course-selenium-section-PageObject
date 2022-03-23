from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Empty basket text not found"

    def should_not_to_be_items_into_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "should be no items in the basket"
