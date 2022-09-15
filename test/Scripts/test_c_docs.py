import time
from src.TestBase.WebDriverSetup import WebDriverSetup
import os
from src.PageObject.Pages.Filters import Filters
from src.PageObject.Pages.PlanificacionHoraria import PlanificacionHoraria


class Test_imp(WebDriverSetup):

    def test_a_imp(self):
        driver = self.driver
        select_emp = PlanificacionHoraria(driver)
        select_emp.select_employees() # Precondicion --> Haber generado X cantidad de empleados
