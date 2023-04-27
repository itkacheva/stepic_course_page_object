from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PWD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PWD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # страница логина должна содержать текст login
        expected_url = LoginPageLocators.LOGIN_URL
        assert expected_url in self.browser.current_url, "Current URL doesn't count '{}'".format(expected_url)

    def should_be_login_form(self):
        # должна быть форма входа
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # должна быть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"