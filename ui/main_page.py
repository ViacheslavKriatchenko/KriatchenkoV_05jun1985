from ui.conf_page import ConfigPage
from config.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from config.links import Links
from random import randint


class MainPage(ConfigPage, MainPageLocators):

    PAGE_URL = Links.HOST
    locator = MainPageLocators()

    def click_on_catalog(self):
        self.wait.until(
            EC.element_to_be_clickable((self.locator.CATALOG)),
            message='Кнопка не активна'
            ).click()

    def click_on_DHL(self):
        self.wait.until(
            EC.element_to_be_clickable((self.locator.DHL)),
            message="Кнопка не активна"
            ).click()

    def add_item_to_cart(self):
        buttons = self.driver.find_elements(*self.locator.ALL_BUY_BUTTONS)
        num_items_to_add = randint(1, len(buttons))
        for i in range(num_items_to_add+1):
            self.action.move_to_element(buttons[i]).click(buttons[i]).perform()
        return num_items_to_add

    def added_to_cart(self):
        number = self.driver.find_element(*self.locator.CART_ITEM_NUMBER)
        self.action.move_to_element(number).pause(2).perform()
        text = number.text
        return int(text)

    def click_button_element(self):
        self.driver.find_element(*self.locator.CART_BUTTON).click()
        self.driver.find_element(*self.locator.PLACE_AN_ORDER)
        self.wait.until(EC.element_to_be_clickable((self.locator.PLACE_AN_ORDER)))

    def delete_items_in_cart(self):
        delete_symbols = self.driver.find_elements(*self.locator.DELETE_CART_BUTTON)
        del delete_symbols[1::2]
        for symbol in delete_symbols:
            symbol.click()
