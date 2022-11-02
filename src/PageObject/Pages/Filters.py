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
        self.date_from = 'Desde'
        self.date_to = 'Hasta'
        self.empresa = 'IdEmpresa'
        self.sector = 'IdSector'
        self.option = 'option'
        self.day_gen = 'fecha'
        self.sunday = '//*[@id="excluirSabado"]/label'
        self.saturday = '//*[@id="excluirDomingo"]/label'
        self.sun_gen = '//*[@id="tablaEmpleadosYJornadas"]/tr[1]/th[6]/span'
        # '//*[@id="tablaEmpleadosYJornadas"]/tr[1]/th[7]/span'
        self.sat_gen = '//*[@id="tablaEmpleadosYJornadas"]/tr[1]/th[7]/span'

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
        return self.driver.find_element(By.CLASS_NAME, self.day_gen)

    def get_sunday(self):
        return self.driver.find_element(By.XPATH, self.sunday)

    def get_saturday(self):
        return self.driver.find_element(By.XPATH, self.saturday)

    def get_sun_gen(self):
        return self.driver.find_element(By.XPATH, self.sun_gen)

    def get_sat_gen(self):
        return self.driver.find_element(By.XPATH, self.sat_gen)

    # TEST SUITE - FILTROS

    # 1 Case: Seleccionar x elemento de Empresa y de Sector.

    def select_emp_sec(self):
        self.get_empresa().click()
        random_opt = random.choice(self.get_options())
        self.driver.execute_script("arguments[0].click();",
                                   WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(random_opt)))
        self.get_sector().click()
        random_opt_sec = random.choice(self.get_options())
        self.driver.execute_script("arguments[0].click();",
                                   WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(random_opt_sec)))
        # Assert code status 200

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

        fin_date = random_date("1/1/2022", "31/12/2022", random.random())
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
        print(txt_gen_date)
        new_date_value = datetime.datetime.strptime(value_date, '%Y-%m-%d').strftime('%d')
        check_gen_date = str(new_date_value).startswith("0")
        print(check_gen_date)
        if check_gen_date is True:
            new_date_value.replace(new_date_value[0], '', 1)
            print("new_date_value --> ", new_date_value)
        else:
            print("No se encontró ningun cero en la fecha:", new_date_value)
        print(txt_gen_date)
        if txt_gen_date == new_date_value:
            print("Coinciden.")
        else:
            print("No se generó la fecha especificada")
        assert txt_gen_date == new_date_value

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

    def checkbox_sun_sat(self):
        self.get_sunday().click()
        self.get_saturday().click()
        sun_gen = self.get_sun_gen().is_displayed()
        sat_gen = self.get_sat_gen().is_displayed()
        # wait = WebDriverWait(self.driver, 200)
        # Chequear la existencia del elemento
        if sun_gen and sat_gen is True:
            print("Los elementos existen.")
        else:
            print("Desaparecieron.")

        assert sun_gen and sat_gen is True

        # sun_invisible = wait.until(EC.invisibility_of_element(sun_gen))
        # wait.until(EC.invisibility_of_element(sat_gen))

    # @staticmethod
    # def get_base_url():
    #    return base_url
