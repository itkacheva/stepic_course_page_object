from selenium.webdriver.common.by import By

class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")


class LoginPageLocators:
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PWD_1 = (By.NAME, "registration-password1")
    REG_PWD_2 = (By.NAME, "registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert")


class BasketPageLocators:
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
