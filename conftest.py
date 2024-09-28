from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeServise
import pytest


@pytest.fixture()
def driver():
    option = ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    servise = ChromeServise(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=option, service=servise)
    yield driver
    driver.quit()
