from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM    = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADDTOBASKET_BTN      = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME         = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE        = (By.CSS_SELECTOR, ".price_color")
    INBASKET_MESSAGE     = (By.XPATH, "//div[@id='messages']/div[1]")
    INBASKET_PROD_NAME   = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    BASKET_PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[last()]")
    BASKET_PRICE_VALUE   = (By.XPATH, "//div[@id='messages']/div[last()]//strong")
