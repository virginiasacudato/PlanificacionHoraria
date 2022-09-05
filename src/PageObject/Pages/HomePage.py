import time

from selenium.webdriver.common.by import By
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# URL base
base_url = "http://localhost/lenox"


class HomePage:
    # Locators
    def __init__(self, driver):
        self.driver = driver
        self.user = "Usuario"
        self.password = "Password"
        self.btn_ingreso = "btnIngresar"

    # Get Elements
    def get_user(self):
        return self.driver.find_element(By.ID, self.user)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_btn_ingreso(self):
        return self.driver.find_element(By.ID, self.btn_ingreso)

    # Actions | Tests Case
    def login(self, user, password):
        self.get_user().send_keys(user)
        self.get_password().send_keys(password)
        time.sleep(3)

    def click_login(self):
        self.get_btn_ingreso().click()

    # URL base como método estático
    @staticmethod
    def get_base_url():
        return base_url
