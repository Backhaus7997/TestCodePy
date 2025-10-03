
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_ROWS = (By.CSS_SELECTOR, "#tbodyid > tr")
    TOTAL_PRICE = (By.ID, "totalp")
    PLACE_ORDER = (By.XPATH, "//button[normalize-space()='Place Order']")

    # Place Order modal
    PO_NAME = (By.ID, "name")
    PO_COUNTRY = (By.ID, "country")
    PO_CITY = (By.ID, "city")
    PO_CARD = (By.ID, "card")
    PO_MONTH = (By.ID, "month")
    PO_YEAR = (By.ID, "year")
    PO_PURCHASE = (By.XPATH, "//button[normalize-space()='Purchase']")
    PO_OK = (By.XPATH, "//button[normalize-space()='OK']")

    def rows(self):
        return self.driver.find_elements(*self.CART_ROWS)

    def total(self):
        t = self.text_of(self.TOTAL_PRICE)
        return int(t) if t.isdigit() else 0

    def open_place_order(self):
        self.click(self.PLACE_ORDER)
        return self

    def complete_order(self, name="QA Tester", country="AR", city="CBA", card="4111111111111111", month="10", year="2025"):
        self.type(self.PO_NAME, name)
        self.type(self.PO_COUNTRY, country)
        self.type(self.PO_CITY, city)
        self.type(self.PO_CARD, card)
        self.type(self.PO_MONTH, month)
        self.type(self.PO_YEAR, year)
        self.click(self.PO_PURCHASE)
        # Confirmation dialog (SweetAlert), extract order id
        from selenium.webdriver.common.by import By
        conf = self.text_of((By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible p"))
        # conf example: "Id: 12345\nAmount: 790 USD\nCard Number: 4111...\nName: QA Tester\nDate: ..."
        import re
        m = re.search(r"Id:\s*(\d+)", conf)
        order_id = m.group(1) if m else None
        self.click(self.PO_OK)
        return order_id
