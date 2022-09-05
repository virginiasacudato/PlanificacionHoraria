import time

from selenium.webdriver.common.by import By
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

base_url = "http://localhost/lenox"


class PlanificacionHoraria:

    def __init__(self, driver):
        self.driver = driver
        self.horarios = "/html/body/main/aside/section/nav/ul/li[3]/div/label"
        self.planificacion_horaria = "Planificacion horaria"
        self.title = "/html/body/main/section/div[2]/div[1]/h1"
        self.employees = "css=tr:nth-child(3) label"
        self.btn_gen = '//*[@id="formCargaPlanificacionHoraria"]/section/div/div[6]/button'
        self.employees_gen = '//*[@id="tablaEmpleadosYJornadas"]/tr[10]/td[2]/span'
        self.employee_name = '.filaEmpleado:nth-child(4) .nombreEmpleado'
        self.ele_jor = '.jornadaItem:nth-child(2) > .jornadaTexto'
        self.second_ele_jor = '.jornadaItem:nth-child(3) > .jornadaTexto'
        self.color_day_work = '.jornadaEmpleado:nth-child(3)'

        # //*[@id="tablaEmpleadosYJornadas"]/tr[4]/td[2]/span
        # //*[@id="tablaEmpleadosYJornadas"]/tr[6]/td[2]/span  --> TR VA DE 2 EN 2

    def get_horarios(self):
        return self.driver.find_element(By.XPATH, self.horarios)

    def get_planificacion_horaria(self):
        return self.driver.find_element(By.LINK_TEXT, self.planificacion_horaria)

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

    # Actions
    def plan_horaria(self):
        self.get_horarios().click()
        time.sleep(3)
        self.get_planificacion_horaria().click()

    # Select employees
    def select_employees(self):
        def cuenta():
            cuenta.numero += 2
            return cuenta.numero

        cuenta.numero = 0
        emp_selected = []

        for i in range(8):
            emp = self.driver.find_element(By.XPATH,
                                           '//*[@id="tableBodyEmpleados"]/tr[' + str(cuenta()) + ']/td/div/label')
            emp.click()

            emp_selected.append(emp.text)
            print(emp.text)

            # //*[@id="tableBodyEmpleados"]/tr[3]/td/div/label
            # //*[@id="tableBodyEmpleados"]/tr[2]/td/div/label

        time.sleep(3)
        return emp_selected


    # Generate employees
    def generate(self):
        self.get_btn_gen().click()
        time.sleep(10)

    # Check employees generated

    def check_emp_gen(self):
        empleados_obtenidos = []
        employee = self.driver.find_elements(By.XPATH, '//*[@id="tablaEmpleadosYJornadas"]/tr/td/span[@title]')

        for employees in employee:
            empleado = employees.get_attribute("title")
            print(empleado)
            empleados_obtenidos.append(empleado)

    # Case 2: Select an employee and modify full time. Check cell color change.
    # xpath=//tbody[@id='tablaEmpleadosYJornadas']/tr[4]/td[2]/span --> Employee
    # xpath=//tbody[@id='tablaEmpleadosYJornadas']/tr/th[2] --> Table

    # Tener en cuenta de que la celda del color de jornada tiene  un atributo "modificada" que aparecera en "true"
    # solo en caso de que se seleccione una nueva jornada.

    def mod_fulltime_employee(self):
        self.get_table_emp().click()
        # self.get_ele_jor().click()
        color_day_work = self.get_day_work().get_attribute("title")
        jor_color_selected = self.get_ele_jor().get_attribute("title")
        if color_day_work == jor_color_selected:
            self.get_second_ele_jor().click()
        else:
            self.get_ele_jor().click()
            print("No coincide la jornada, primer elemento clic.")

    @staticmethod
    def get_base_url():
        return base_url
