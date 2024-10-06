from selenium.webdriver.support.wait import WebDriverWait
import allure
from selenium.webdriver import ActionChains


class ConfigPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        self.action = ActionChains(driver)

    def open_the_page(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)
