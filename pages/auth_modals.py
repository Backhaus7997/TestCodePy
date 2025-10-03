from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

class AuthModals(BasePage):
    # Signup modal
    SIGNUP_USERNAME = (By.ID, "sign-username")
    SIGNUP_PASSWORD = (By.ID, "sign-password")
    SIGNUP_CONFIRM  = (By.XPATH, "//div[@id='signInModal']//button[text()='Sign up']")

    # Login modal
    LOGIN_USERNAME  = (By.ID, "loginusername")
    LOGIN_PASSWORD  = (By.ID, "loginpassword")
    LOGIN_CONFIRM   = (By.XPATH, "//div[@id='logInModal']//button[text()='Log in']")

    MODAL_CLOSES    = (By.XPATH, "//div[contains(@class,'modal') and contains(@style,'display: block')]")

    def signup(self, username, password):
        self.type(self.SIGNUP_USERNAME, username)
        self.type(self.SIGNUP_PASSWORD, password)
        self.click(self.SIGNUP_CONFIRM)
       
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            _ = alert.text  
            alert.accept()
        except TimeoutException:
            raise AssertionError(
                "No apareció el alert luego de 'Sign up'. Probá subir el --wait (p.ej. --wait 20) o reintentar."
            )
        return self

    def login(self, username, password):
        self.type(self.LOGIN_USERNAME, username)
        self.type(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_CONFIRM)
        
        self.wait.until(EC.invisibility_of_element_located(self.MODAL_CLOSES))
        return self
