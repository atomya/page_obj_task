from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage

def test_guest_can_add_product_to_basket:
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()