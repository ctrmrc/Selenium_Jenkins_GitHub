from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage

def test_guests_can_add_product_to_basket(driver):
    url = ProductPageLocators.PRODUCT_PAGE_LINK
    page = ProductPage(driver, url)
    page.open()

    page.guests_can_add_product_to_basket()

def test_user_can_add_product_to_basket(driver):
    url = LoginPageLocators.LOGIN_PAGE_LINK
    page = LoginPage(driver, url)
    page.open()

    email, password = page.generate_email_n_password()
    page.guests_can_register(email, password)

    url = ProductPageLocators.PRODUCT_PAGE_LINK
    page = ProductPage(driver, url)
    page.open()
    page.user_can_add_product_to_basket()