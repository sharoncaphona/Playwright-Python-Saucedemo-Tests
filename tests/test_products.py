#tests/test_products.py

from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_addproduct_to_cart(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)

    page.click(home.add_to_cart_button.format("sauce-labs-backpack"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '1'

    page.click(home.add_to_cart_button.format("sauce-labs-bike-light"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '2'

    page.click(home.add_to_cart_button.format("sauce-labs-bolt-t-shirt"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '3'

    page.click(home.add_to_cart_button.format("test.allthethings()-t-shirt-(red)"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '4'

    page.click(home.add_to_cart_button.format("sauce-labs-fleece-jacket"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '5'

    page.click(home.add_to_cart_button.format("sauce-labs-onesie"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '6'

def test_removeproduct_from_cart(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)

    # First, add products to the cart
    page.click(home.add_to_cart_button.format("sauce-labs-backpack"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    page.click(home.add_to_cart_button.format("sauce-labs-bike-light"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    page.click(home.add_to_cart_button.format("sauce-labs-bolt-t-shirt"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    page.click(home.add_to_cart_button.format("test.allthethings()-t-shirt-(red)"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    page.click(home.add_to_cart_button.format("sauce-labs-fleece-jacket"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    page.click(home.add_to_cart_button.format("sauce-labs-onesie"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '6'

    # Now, remove products one by one and check the cart count
    page.click(home.remove_from_cart_button.format("sauce-labs-backpack"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '5'

    page.click(home.remove_from_cart_button.format("sauce-labs-bike-light"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '4'

    page.click(home.remove_from_cart_button.format("sauce-labs-bolt-t-shirt"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '3'

    page.click(home.remove_from_cart_button.format("test.allthethings()-t-shirt-(red)"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '2'

    page.click(home.remove_from_cart_button.format("sauce-labs-fleece-jacket"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == '1'

    page.click(home.remove_from_cart_button.format("sauce-labs-onesie"))
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == ''