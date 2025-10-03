from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//a[normalize-space()='Add to cart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name")
    PRICE = (By.CSS_SELECTOR, ".price-container")

    def add_to_cart(self):
        
        self.present(self.PRODUCT_NAME)

        
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        self.driver.execute_script("arguments[0].click();", btn)

        
        try:
            self.wait.until(EC.alert_is_present())
        except TimeoutException:
            time.sleep(0.7)
            self.driver.execute_script("arguments[0].click();", btn)
            self.wait.until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        _ = alert.text
        alert.accept()
        return self

    def product_name(self):
        return self.text_of(self.PRODUCT_NAME)

    def product_price_value(self):
        raw = self.text_of(self.PRICE)
        import re
        m = re.search(r"\$(\d+)", raw)
        return int(m.group(1)) if m else 0