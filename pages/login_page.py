from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "url not login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASS), "Password_1 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASS_DUB), "Password_2 field is not presented"
        p_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        p_email.send_keys(email)
        p_pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS)
        p_pass1.send_keys(password)
        p_pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_DUB)
        p_pass2.send_keys(password)
        p_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        p_button.click()
