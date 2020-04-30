from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_PRODUCT)
        button.click()

