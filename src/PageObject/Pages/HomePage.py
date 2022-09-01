import time

from selenium.webdriver.common.by import By
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# URL base
BASE_URL = os.environ.get("URL")


class HomePage:
    # Locators
    def __init__(self, driver):
        self.driver = driver
        self.user = "Usuario"
        self.password = "Password"
        self.btn_ingreso = "btnIngresar"
        self.horarios = "/html/body/main/aside/section/nav/ul/li[3]/div/label"
        self.planificacion_horaria = "Planificacion horaria"
        self.title = "/html/body/main/section/div[2]/div[1]/h1"

    # Get Elements
    def get_user(self):
        return self.driver.find_element(By.ID, self.user)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_btn_ingreso(self):
        return self.driver.find_element(By.ID, self.btn_ingreso)

    def get_horarios(self):
        return self.driver.find_element(By.XPATH, self.horarios)

    def get_planificacion_horaria(self):
        return self.driver.find_element(By.LINK_TEXT, self.planificacion_horaria)

    def get_title(self):
        return self.driver.find_element(By.XPATH, self.title)

    # Actions | Tests Case
    def login(self, user, password):
        self.get_user().send_keys(user)
        self.get_password().send_keys(password)
        time.sleep(3)

    def click_login(self):
        self.get_btn_ingreso().click()

    def plan_horaria(self):
        self.get_horarios().click()
        time.sleep(3)
        self.get_planificacion_horaria().click()

    # URL base como método estático
    @staticmethod
    def get_base_url():
        return BASE_URL
