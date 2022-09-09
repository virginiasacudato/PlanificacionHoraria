# import time

from selenium.webdriver.common.by import By
# from os.path import join, dirname
# from dotenv import load_dotenv
import random
from random import choice


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
        random_opt.click()
        self.get_sector().click()
        for optiontwo in self.get_options():
            print(optiontwo.text)
        random_opt_sec = random.choice(self.get_options())
        print(random_opt_sec)
        random_opt_sec.click()

    # 2 Case: Seleccionar x fecha desde/hasta
    def select_date(self):
        def random_date():
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                    '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
            years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                     '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028']

            rand_date = '{}.{}.{}'.format(*map(choice, [days, months, years]))
            return rand_date()
        print(random_date())

        self.get_date_to().send_key(str(random_date()))

    # 3 Case: Seleccionar empresa
    def select_empresa(self):
        self.get_empresa().click()
        for option in self.get_options():
            print(option.text)

        random_opt = random.choice(self.get_options())
        print(random_opt)
        random_opt.click()

    # 4 Case: Seleccionar sector
    def select_sec(self):
        self.get_sector().click()
        for optiontwo in self.get_options():
            print(optiontwo.text)
        random_opt_sec = random.choice(self.get_options())
        print(random_opt_sec)
        random_opt_sec.click()

    # 5 Case: Checks excluir Sabados y domingos.
    # (A partir de aca se generan los siguientes casos en un entorno despues de haber generado X empleados)









    # @staticmethod
    # def get_base_url():
    #    return base_url
