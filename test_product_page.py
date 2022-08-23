from .pages.product_page import MainPage
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link) 
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    
    page.shoud_be_messege_that_item_added_to_basket()
    page.shoud_be_price_messege()

 