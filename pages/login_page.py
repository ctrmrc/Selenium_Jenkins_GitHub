from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def guests_can_see_go_to_login_page_button(self):
        self.driver.find_element(*LoginPageLocators.BUTTON_GO_TO_LOGIN_PAGE)

    def generate_email_n_password(self):
        return (str(time.time()) + '@fakemail.org', 'pass_6789')

    def guests_can_register(self, email, password):
        self.email = email
        self.password = password

        self.driver.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSOWRD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(password)

        self.driver.find_element(*LoginPageLocators.BUTTON_FINISH_REGISTRATION).click()