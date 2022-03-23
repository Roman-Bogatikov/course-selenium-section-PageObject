from .locators import MainPageLocators
from .login_page import LoginPage

from .base_page import BasePage
from .basket_page import BasketPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def go_to_basked_check_empty(self):
    #     self.should_be_basket_link()
    #     self.go_to_basket_page()
    #     basket_page = BasketPage(browser=self.browser, url=self.browser.current_url)
    #     basket_page.should_not_to_be_items_into_basket()
    #     basket_page.should_be_empty_basket_text()
