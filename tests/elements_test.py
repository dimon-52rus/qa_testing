import time
from conftest import driver
from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:
        def test(self, driver):
            page = TextBoxPage(driver, "https://demoqa.com/automation-practice-form")
            page.open()
            page.fill_all_fields()
            time.sleep(5)

