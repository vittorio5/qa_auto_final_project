from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        # prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        prod_name = self.get_product_name()
        prod_price = self.get_product_price()        
        self.browser.find_element(*ProductPageLocators.ADDTOBASKET_BTN).click()
        self.solve_quiz_and_get_code()
        self.is_correct_product(prod_name)
        self.is_correct_price(prod_price)
    
    def is_correct_product(self, prod_name):
        # проверка, что есть сообщение о добавлении в корзину
        assert self.is_element_present(*ProductPageLocators.INBASKET_MESSAGE), "Message about product in basket wasn't found"
        # проверка, что у товара корректное название
        assert prod_name == self.browser.find_element(*ProductPageLocators.INBASKET_PROD_NAME).text, "Product name is wrong!"
    
    def is_correct_price(self, prod_price):
        # проверка, что есть сообщение со стоимостью корзины
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), "Message with basket price wasn't found"
        # проверка, что стоимость корзины совпадает с ценой товара
        assert prod_price == self.browser.find_element(*ProductPageLocators.BASKET_PRICE_VALUE).text, "Product price is wrong!"
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
