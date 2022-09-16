from selenium.webdriver.common.by import By
import random
import time
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Filters:

    def __init__(self, driver):
        # Locators
        self.driver = driver
        self.print_btn = 'printBtn'
        self.img = 'image'

    # Get Elements
    def get_print_btn(self):
        return self.driver.find_element(By.ID, self.print_btn)

    def get_doc_gen(self):
        return self.driver.find_element(By.ID, self.img)

    # Actions
    def print(self):
        self.get_print_btn().click()

    def check_print(self):



