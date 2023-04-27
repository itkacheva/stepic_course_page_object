from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    PRODUCT_NAME = None
    PRICE = None
    PROMO_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"

    def should_not_be_success_message(self):
        # проверяем отсутствие алертов о добавлении товара в корзину
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), \
            "Alert Product is presented, but should not be"
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRICE), \
            "Alert Price is presented, but should not be"

    def should_be_add_button(self):
        # проверка налиия кнопки Добавить в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def save_product_name_and_price(self):
        # запоминаем имя продукта и его цену на странице товара
        ProductPage.PRODUCT_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        ProductPage.PRICE = self.browser.find_element(*ProductPageLocators.PRICE).text

    def click_to_add_button(self):
        # добавляем продукт в корзину
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_alerts_about_add_product(self):
        # проверяем наличие алертов о добавлении товаров с именем и ценой
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), "Alert Product is not presented"
        assert self.is_element_present(*ProductPageLocators.ALERT_PRICE), "Alert Price is not presented"

    def check_product_name_and_price_in_basket(self):
        # проверяем, что имя товара и его цена верные
        assert ProductPage.PRODUCT_NAME in \
               self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text, \
               "Product '{}' doesn't add".format(ProductPage.PRODUCT_NAME)
        assert ProductPage.PRICE in self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text, \
               "Product '{}' add with incorrect price '{}'".format(ProductPage.PRODUCT_NAME, ProductPage.PRICE)

    def success_message_should_disappear(self):
        # проверяем, что алерты о добавлении товара в корзину есть, а потом пропадают
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_NAME), "Alert Product doesn't disappeared"
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRICE), "Alert Price doesn't disappeared"
