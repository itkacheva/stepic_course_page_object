from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    LINK = "https://selenium1py.pythonanywhere.com/catalogue/"

    def go_to_login_page(self):
        # переходим на страницу логина
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        # проверяем наличие ссылки перехода на страницу логина
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_basket_link(self):
        # проверяем наличие ссылки перехода на страницу корзины
        assert self.is_element_present(*MainPageLocators.BASKET_LINK), "Basket link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()
