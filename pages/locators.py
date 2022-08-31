from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FORM2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")

class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    BOOK_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")
    BOOK_IN_BASKET = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_MESSEGE = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") 
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    