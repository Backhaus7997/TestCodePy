
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_cart_prices_and_total(driver, base_url, wait_seconds):
    home = HomePage(driver, base_url, wait_seconds).open_home()
    product = ProductPage(driver, base_url, wait_seconds)

    # Añadir dos productos conocidos para poder calcular el total esperado
    home.open_category("Phones").open_product("Samsung galaxy s6")
    p1 = product.product_price_value()
    product.add_to_cart()

    home.open_home().open_category("Monitors").open_product("Apple monitor 24")
    p2 = product.product_price_value()
    product.add_to_cart()

    home.go_cart()
    cart = CartPage(driver, base_url, wait_seconds)

    total_ui = cart.total()
    expected = p1 + p2
    assert total_ui == expected, f"Total UI {total_ui} != esperado {expected}"
