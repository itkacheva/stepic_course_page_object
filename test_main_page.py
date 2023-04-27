import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # @pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MainPage.LINK)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                 # открываем страницу
        page.should_be_login_link()                 # проверяем наличие ссылки перехода на страницу логина
        page.go_to_login_page()                     # переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # инициализируем Login Page
        login_page.should_be_login_page()           # проверяем на странице логина адрес, формы входа и регистрации

    @pytest.mark.basket
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, MainPage.LINK)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                 # открываем страницу
        page.should_be_basket_link()                # проверяем наличие ссылки перехода в корзину
        page.go_to_basket_page()                    # переходим в корзину
        basket_page = BasketPage(browser, browser.current_url) # инициализируем BasketPage
        basket_page.should_not_be_text()            # ожидаем, что есть текст о том что корзина пуста
        basket_page.should_not_be_products()        # ожидаем, что в корзине нет товаров

