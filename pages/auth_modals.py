
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class AuthModals(BasePage):
    # Signup modal
    SIGNUP_USERNAME = (By.ID, "sign-username")
    SIGNUP_PASSWORD = (By.ID, "sign-password")
    SIGNUP_CONFIRM = (By.XPATH, "//div[@id='signInModal']//button[text()='Sign up']")

    # Login modal
    LOGIN_USERNAME = (By.ID, "loginusername")
    LOGIN_PASSWORD = (By.ID, "loginpassword")
    LOGIN_CONFIRM = (By.XPATH, "//div[@id='logInModal']//button[text()='Log in']")

    MODAL_CLOSES = (By.XPATH, "//div[contains(@class,'modal') and contains(@style,'display: block')]")

    def signup(self, username, password):
        self.type(self.SIGNUP_USERNAME, username)
        self.type(self.SIGNUP_PASSWORD, password)
        self.click(self.SIGNUP_CONFIRM)
        # Demoblaze usa alert() de browser para feedback
        alert = self.driver.switch_to.alert
        alert.accept()
        return self

    def login(self, username, password):
        self.type(self.LOGIN_USERNAME, username)
        self.type(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_CONFIRM)
        # Esperar a que desaparezca el modal
        self.wait.until(EC.invisibility_of_element_located(self.MODAL_CLOSES))
        return self
