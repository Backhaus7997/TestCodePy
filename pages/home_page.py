
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SIGNUP_BTN = (By.ID, "signin2")
    LOGIN_BTN = (By.ID, "login2")
    CART_LINK = (By.ID, "cartur")
    USER_GREETING = (By.ID, "nameofuser")

    CATEGORY_LINK = lambda self, name: (By.XPATH, f"//a[@id='itemc' and normalize-space()='{name}']")
    PRODUCT_LINK = lambda self, name: (By.XPATH, f"//a[@class='hrefch' and normalize-space()='{name}']")

    def open_home(self):
        return self.open("")

    def open_category(self, name):
        self.click(self.CATEGORY_LINK(name))
        return self

    def open_product(self, name):
        self.click(self.PRODUCT_LINK(name))
        return self

    def go_cart(self):
        self.click(self.CART_LINK)
        return self

    def open_login(self):
        self.click(self.LOGIN_BTN)
        return self

    def open_signup(self):
        self.click(self.SIGNUP_BTN)
        return self

    def greeting_text(self):
        return self.text_of(self.USER_GREETING)
