from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_two_products_to_cart(driver, base_url, wait_seconds):
    home = HomePage(driver, base_url, wait_seconds).open_home()
    product = ProductPage(driver, base_url, wait_seconds)

    home.open_category("Phones").open_product("Samsung galaxy s6")
    price1 = product.product_price_value()
    product.add_to_cart()

    home.open_home().open_category("Laptops").open_product("Sony vaio i5")
    price2 = product.product_price_value()
    product.add_to_cart()

    home.go_cart()
    cart = CartPage(driver, base_url, wait_seconds)
    cart.wait_for_min_rows(2)
    assert len(cart.rows()) >= 2