import time

from selenium.webdriver.common.by import By
import re

class PlanificacionHoraria:

    def __init__(self, driver):
        # Locators
        self.driver = driver
        self.title = "/html/body/main/section/div[2]/div[1]/h1"
        self.employees = "css=tr:nth-child(3) label"
        self.btn_gen = '//*[@id="formCargaPlanificacionHoraria"]/section/div/div[6]/button'
        self.employees_gen = '//*[@id="tablaEmpleadosYJornadas"]/tr[10]/td[2]/span'
        self.employee_name = '.filaEmpleado:nth-child(4) .nombreEmpleado'
        self.ele_jor = '.jornadaItem:nth-child(2) > .jornadaTexto'
        self.second_ele_jor = '.jornadaItem:nth-child(3) > .jornadaTexto'
        self.color_day_work = '.jornadaEmpleado:nth-child(3)'
        self.save_btn = 'aplicarCambios'
        self.select_day = '//*[@id="tablaEmpleadosYJornadas"]/tr[4]/td[4]'

    # Get elements
    def get_title(self):
        return self.driver.find_element(By.XPATH, self.title)

    def get_btn_gen(self):
        return self.driver.find_element(By.XPATH, self.btn_gen)

    def get_ele_jor(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ele_jor)

    def get_second_ele_jor(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.second_ele_jor)

    def get_table_emp(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.employee_name)

    def get_day_work(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.color_day_work)

    def save_btn_changes(self):
        return self.driver.find_element(By.ID, self.save_btn)

    # Actions

    # TEST SUITE - JORNADAS
    def select_employees(self):
        def cuenta():
            cuenta.numero += 2
            return cuenta.numero

        def replaceString(text):
            return re.sub(r'\([^)]*\)', '', str(text))

        cuenta.numero = 0
        global emp_selected
        global new_list_emp_sele
        emp_selected = []
        new_list_emp_sele = []

        for i in range(8):
            emp = self.driver.find_element(By.XPATH,
                                           '//*[@id="tableBodyEmpleados"]/tr[' + str(cuenta()) + ']/td/div/label')
            emp.click()
            emp_selected.append(emp.text)

        replacestr = [replaceString(s) for s in emp_selected]
        for x in replacestr:
            es_mayus = x.isupper()
            if es_mayus is True:
                x.upper()
                new_list_emp_sele.append(x.strip())

        print(new_list_emp_sele)

        time.sleep(3)
        # return emp_selected

    # Generate employees
    def generate(self):
        self.get_btn_gen().click()
        time.sleep(10)

    # Check employees generated

    def check_emp_gen(self):
        # Conserva unicamente el nombre en el array
        def replace_string(text):
            return re.sub(r'\nLegajo: \d*', "", str(text))

        empleados_obtenidos = []
        employee = self.driver.find_elements(By.XPATH, '//*[@id="tablaEmpleadosYJornadas"]/tr/td/span[@title]')

        # Recorre la la lista de emp. generados y obtiene el atributo title
        for employees in employee:
            empleado = employees.get_attribute("title")
            empleados_obtenidos.append(empleado)  # Almecena el valor obtenido en el array

        new_emp_obt = [replace_string(s) for s in empleados_obtenidos]
        print(new_emp_obt)

        check = any(item in new_emp_obt for item in new_list_emp_sele)

        if check:
            print("Se generaron algunos empleados seleccionados.")
        else:
            print("Ningun empleado con calendario asignado.")

        assert check == True

    # Case 2: Select an employee and modify full time. Check cambio de jornada.

    def mod_fulltime_employee(self):
        self.get_table_emp().click()
        # self.get_ele_jor().click()
        global jor_color_selected
        color_day_work = self.get_day_work().get_attribute("title")
        jor_color_selected = self.get_ele_jor().get_attribute("title")
        if color_day_work == jor_color_selected:
            self.get_second_ele_jor().click()
        else:
            self.get_ele_jor().click()


    def save_changes(self):
        self.get_btn_gen().click()
        # Podria verificar el texto del modal exitoso

    # Case 3: Modify specific days
    def mod_spec_days(self):

        def cuenta():
            cuenta.numero += 3
            return cuenta.numero

        color_day = []
        cuenta.numero = 0

        for i in range(2):
            day_jornada = self.driver.find_element(By.XPATH, '//*[@id="tablaEmpleadosYJornadas"]/tr[4]/td[' + str(
                cuenta()) + ']/div')
            day_jornada.click()
            color_day.append(day_jornada.get_attribute("title"))
        print(color_day)
        self.get_ele_jor().click()


