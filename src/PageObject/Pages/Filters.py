# import time

from selenium.webdriver.common.by import By
# from os.path import join, dirname
# from dotenv import load_dotenv
import random

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# base_url = "http://localhost/lenox"


class Filters:

    def __init__(self, driver):
        # Locators
        self.driver = driver
        self.date_from = 'Desde'
        self.date_to = 'Hasta'
        self.empresa = 'IdEmpresa'
        self.sector = 'IdSector'
        self.option = 'option'

    # Get elements
    def get_date_from(self):
        return self.driver.find_element(By.ID, self.date_from)

    def get_date_to(self):
        return self.driver.find_element(By.ID, self.date_to)

    def get_empresa(self):
        return self.driver.find_element(By.ID, self.empresa)

    def get_sector(self):
        return self.driver.find_element(By.ID, self.sector)

    def get_options(self):
        return self.driver.find_elements(By.TAG_NAME, self.option)

    # TEST SUITE - FILTROS

    # 1 Case: Seleccionar x elemento de Empresa y de Sector.

    def select_emp_sec(self):
        self.get_empresa().click()
        for option in self.get_options():
            print(option.text)

        random_opt = random.choice(self.get_options())
        print(random_opt)

    # @staticmethod
    # def get_base_url():
    #    return base_url
