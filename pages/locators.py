from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK         = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK        = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON          = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM       = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM    = (By.CSS_SELECTOR, "#register_form")
    EMAIL            = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD         = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON  = (By.CSS_SELECTOR, "[value='Register']")
    
class ProductPageLocators():
    ADDTOBASKET_BTN      = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME         = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE        = (By.CSS_SELECTOR, ".price_color")
    INBASKET_MESSAGE     = (By.XPATH, "//div[@id='messages']/div[1]")
    INBASKET_PROD_NAME   = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    BASKET_PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[last()]")
    BASKET_PRICE_VALUE   = (By.XPATH, "//div[@id='messages']/div[last()]//strong")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE  = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")
    BASKET_SUMMARY_MODULE = (By.CSS_SELECTOR, ".basket_summary")
