from .pages.login_page import LoginPage
from .pages.locators import BasePageLocators

def test_guests_can_see_go_to_login_page_button(driver):
    url = BasePageLocators.MAIN_PAGE_LINK
    page = LoginPage(driver, url)
    page.open()

    page.guests_can_see_go_to_login_page_button()

