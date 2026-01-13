#tests/test_login.py

from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_locked_login(page):
    login = LoginPage(page)
    login.open() 
    login.login("locked_out_user", "secret_sauce")
    error_message = page.text_content("h3[data-test='error']")
    assert error_message == "Epic sadface: Sorry, this user has been locked out."

def test_invalid_password(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "wrong_password")
    error_message = page.text_content("h3[data-test='error']")
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

def test_invalid_username(page):
    login = LoginPage(page)
    login.open() 
    login.login("wrong_user", "secret_sauce")
    error_message = page.text_content("h3[data-test='error']")
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

def test_empty_credentials(page):
    login = LoginPage(page)
    login.open() 
    login.login("", "")
    error_message = page.text_content("h3[data-test='error']")
    assert error_message == "Epic sadface: Username is required"

def test_logout(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    login.logout()
    assert page.url == "https://www.saucedemo.com/"