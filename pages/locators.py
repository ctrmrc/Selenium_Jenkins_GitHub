from selenium.webdriver.common.by import By as by

class BasePageLocators():
    MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/'

class ProductPageLocators():
    PRODUCT_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    BUTTON_ADD_TO_BASKET = (by.XPATH, '//button[@value="Add to basket"]')
    PRODUCTS_NAME = (by.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    PRODUCTS_PRICE = (by.XPATH, '(//p[@class="price_color"])[1]')
    PRODUCT_IN_BASKET_NAME = (by.XPATH, '(//div[@class="alertinner "]//strong)[1]')
    PRODUCT_IN_BASKET_PRICE = (by.XPATH, '(//div[@class="alertinner "]//strong)[3]')

class LoginPageLocators():
    LOGIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    BUTTON_GO_TO_LOGIN_PAGE = (by.ID, 'login_link1')
    REGISTRATION_EMAIL = (by.ID, 'id_registration-email')
    REGISTRATION_PASSOWRD = (by.ID, 'id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD = (by.ID, 'id_registration-password2')
    BUTTON_FINISH_REGISTRATION = (by.XPATH, '//button[@name="registration_submit"]')
