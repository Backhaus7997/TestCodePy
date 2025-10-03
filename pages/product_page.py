
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//a[normalize-space()='Add to cart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name")
    PRICE = (By.CSS_SELECTOR, ".price-container")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)
        alert = self.driver.switch_to.alert
        alert.accept()
        return self

    def product_name(self):
        return self.text_of(self.PRODUCT_NAME)

    def product_price_value(self):
        # Ejemplo de texto: "Price: $360 *includes tax"
        raw = self.text_of(self.PRICE)
        import re
        m = re.search(r"\$(\d+)", raw)
        return int(m.group(1)) if m else 0
