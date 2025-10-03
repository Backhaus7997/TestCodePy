
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_checkout_happy_path(driver, base_url, wait_seconds):
    home = HomePage(driver, base_url, wait_seconds).open_home()
    product = ProductPage(driver, base_url, wait_seconds)

    # Añadir un item y completar la orden
    home.open_category("Laptops").open_product("MacBook air")
    product.add_to_cart()

    home.go_cart()
    cart = CartPage(driver, base_url, wait_seconds)
    cart.open_place_order()
    order_id = cart.complete_order(name="Martin QA", country="AR", city="Cordoba", card="4111111111111111", month="10", year="2025")
    assert order_id is not None and order_id.isdigit()
