
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url, wait_seconds=10):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, wait_seconds)

    def open(self, path=""):
        self.driver.get(self.base_url + path)
        return self

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def type(self, locator, text, clear=True):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(text)
        return el

    def text_of(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def present(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return True
