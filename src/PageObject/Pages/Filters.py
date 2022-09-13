# import time

from selenium.webdriver.common.by import By
# from os.path import join, dirname
# from dotenv import load_dotenv
import random
import time
import datetime


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
        self.day_gen = '.fechas:nth-child(3) > .fecha'

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

    def get_body(self):
        return self.driver.find_element(By.TAG_NAME, 'body')

    def get_day_gen(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.day_gen)

    # TEST SUITE - FILTROS

    # 1 Case: Seleccionar x elemento de Empresa y de Sector.

    def select_emp_sec(self):
        self.get_empresa().click()
        for option in self.get_options():
            print(option.text)

        random_opt = random.choice(self.get_options())
        # print(random_opt)
        random_opt.click()
        self.get_sector().click()
        # for optiontwo in self.get_options():
        # print(optiontwo.text)
        random_opt_sec = random.choice(self.get_options())
        # print(random_opt_sec)
        random_opt_sec.click()

    # 2 Case: Seleccionar x fecha desde/hasta
    def select_date(self):
        # Seleccion de fecha aleatoria segun un rango de fechas
        def str_time_prop(start, end, time_format, prop):
            stime = time.mktime(time.strptime(start, time_format))
            etime = time.mktime(time.strptime(end, time_format))

            ptime = stime + prop * (etime - stime)

            return time.strftime(time_format, time.localtime(ptime))

        def random_date(start, end, prop):
            return str_time_prop(start, end, '%d/%m/%Y', prop)  # Formato Day-Month-Year

        fin_date = random_date("1/1/2020", "1/1/2021", random.random())
        print(fin_date)
        # Envio de date aleatoria a input
        self.get_date_from().send_keys(fin_date)
        self.driver.execute_script("arguments[0].setAttribute('value'," + str(fin_date) + ")", self.get_date_from())
        # self.get_date_from().set_attribute('value', str(fin_date))

    # El chequeo del empleado tiene que ser despues de la generacion del empleado
    def check_filter_date(self):
        self.get_body().click()
        value_date = self.get_date_from().get_attribute("value")
        txt_gen_date = self.get_day_gen().text
        check_gen_date = str(txt_gen_date).startswith("0")
        if check_gen_date is True:
            str(txt_gen_date).replace('0', '')
            print(txt_gen_date)
        else:
            print("No se encontró ningun cero en la fecha:", txt_gen_date)
        new_date_value = datetime.datetime.strptime(value_date, '%Y-%m-%d').strftime('%d')
        print(new_date_value)


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
