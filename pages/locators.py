from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ALERTINNERS = (By.CSS_SELECTOR, ".alertinner strong")
    ALERTINNER_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ALERTINNER_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
