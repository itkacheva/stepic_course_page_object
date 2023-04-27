from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_text(self):
        # проверка наличия текста о пустой корзине
        text = self.browser.find_element(*BasketPageLocators.CONTENT_INNER).text
        assert "basket is empty" in text, "Basket doesn't empty. '{}'".format(text)

    def should_not_be_products(self):
        # проверка отсутствия товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket Items is presented, but should not be"