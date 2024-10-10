from ui.conf_page import ConfigPage
from config.locators import CartPageLocators
from config.links import Links


class CartPage(ConfigPage, CartPageLocators):
    PAGE_URL = Links.CART_URL
    locator = CartPageLocators()

    def delete_items_in_cart(self):
        deletes = self.driver.find_elements(*self.locator.DELETE_CART_BUTTONs)
        for delete in deletes:
            delete.click()

    def basket(self):
        total = self.driver.find_element(*self.locator.TOTAL_AMOUNT)
        return total.text
