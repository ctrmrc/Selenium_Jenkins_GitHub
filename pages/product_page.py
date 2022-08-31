from .base_page import BasePage
from .locators import ProductPageLocators
from .login_page import LoginPage

class ProductPage(BasePage):
    def guests_can_add_product_to_basket(self):
        self.driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def user_can_add_product_to_basket(self):
        self.driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

        products_name = self.driver.find_element(*ProductPageLocators.PRODUCTS_NAME).text
        products_price = self.driver.find_element(*ProductPageLocators.PRODUCTS_PRICE).text

        self.wait_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME)

        product_in_basket_name = self.driver.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME).text
        product_in_basket_price = self.driver.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE).text

        assert products_name == product_in_basket_name, 'Product names must be identical'
        assert products_price == product_in_basket_price, 'Product prices must be identical'

