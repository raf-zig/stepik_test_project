from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON)
        basket_button.click() 

    def shoud_be_messege_that_item_added_to_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET)
        assert book_name.text == book_in_basket.text, "не равно"
  
    def shoud_be_price_messege(self):
        price_messege = self.browser.find_element(*ProductPageLocators.PRICE_MESSEGE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)  
        assert price_messege.text == price_in_basket.text, "не равно"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME), \
            "Success message is presented, but should not be"

    def should_disappeare_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_NAME), \
            "Success message is presented"