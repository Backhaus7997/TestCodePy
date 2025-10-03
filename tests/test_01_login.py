
import pytest
from pages.home_page import HomePage
from pages.auth_modals import AuthModals
from utils.data import unique_username, User

@pytest.mark.smoke
def test_successful_signup_and_login(driver, base_url, wait_seconds):
    home = HomePage(driver, base_url, wait_seconds).open_home()
    auth = AuthModals(driver, base_url, wait_seconds)

    user = User(username=unique_username("user"), password="Passw0rd!")

    # Signup
    home.open_signup()
    auth.signup(user.username, user.password)

    # Login
    home.open_login()
    auth.login(user.username, user.password)

    # Validar saludo con nombre
    assert user.username in home.greeting_text()
