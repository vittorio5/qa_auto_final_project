from .base_page import BasePage
from .locators import BasketPageLocators
import time


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        self.should_not_be_products()
        self.should_be_message_about_empty_basket()
    
    def should_not_be_products(self):
        # проверка, что нет товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_MODULE), "There are products in basket, but shouldn't be!"

    def should_be_message_about_empty_basket(self):
        # проверка, что есть текст о пустой корзине
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no message about empty basket!"
