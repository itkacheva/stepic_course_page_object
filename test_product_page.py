import time
import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LoginPage.LINK)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "!@#$%^DFG"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.should_not_be_success_message()            # ожидаем, что там нет алертов об успешном добавлении в корзину
        page.should_be_add_button()                     # проверяем наличие кнопки Добавить в корзину
        page.save_product_name_and_price()              # запоминаем имя товара и его цену
        page.click_to_add_button()                      # кликаем на кнопку Добавить в корзину
        page.should_be_alerts_about_add_product()       # проверяем появление алертов об успешном добавлении в корзину
        page.check_product_name_and_price_in_basket()   # проверяем что в корзине товар с верным наименованием и ценой
        # page.success_message_should_disappear()       # проверяем, что алерты есть на странице и должны исчезнуть

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.PROMO_LINK)
    page.open()
    page.click_to_add_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()            # ожидаем, что там нет алертов об успешном добавлении в корзину

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.LINK)
    page.open()
    page.click_to_add_button()
    page.success_message_should_disappear()         # проверяем, что алерты есть на странице и должны исчезнуть

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = MainPage(browser, ProductPage.LINK)              # инициализируем Page Object
    page.open()                                             # открываем страницу
    page.should_be_basket_link()                            # проверяем наличие ссылки перехода в корзину
    page.go_to_basket_page()                                # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)  # инициализируем BasketPage
    basket_page.should_not_be_text()                        # ожидаем, что есть текст о том что корзина пуста
    basket_page.should_not_be_products()                    # ожидаем, что в корзине нет товаров

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.LINK)               # инициализируем Page Object
    page.open()                                     # открываем страницу
    page.should_be_add_button()                     # проверяем наличие кнопки Добавить в корзину
    page.save_product_name_and_price()              # запоминаем имя товара и его цену
    page.click_to_add_button()                      # кликаем на кнопку Добавить в корзину
    page.should_be_alerts_about_add_product()       # проверяем появление алертов об успешном добавлении в корзину
    page.check_product_name_and_price_in_basket()   # проверяем что в корзине товар с верным наименованием и ценой
