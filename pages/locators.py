from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ItemPageLocators():
    BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    BOOK_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")
    BOOK_IN_BASKET = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_MESSEGE = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".product_main .price_color") 