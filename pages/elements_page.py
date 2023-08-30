import time

from locators.element_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FIRST_NAME).send_keys("dfsfsd")
        self.element_is_visible(self.locators.LAST_NAME).send_keys("sdfds")
        self.element_is_visible(self.locators.EMAIL).send_keys("saasd@ya.ru")
