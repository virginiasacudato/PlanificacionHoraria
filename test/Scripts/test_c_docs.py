import time
from src.TestBase.WebDriverSetup import WebDriverSetup
import os
from src.PageObject.Pages.Filters import Filters
from src.PageObject.Pages.PlanificacionHoraria import PlanificacionHoraria
from src.PageObject.Pages.Docs import Docs


class Test_imp(WebDriverSetup):

    def test_a_imp(self):
        driver = self.driver
        select_emp = PlanificacionHoraria(driver)
        docs = Docs(driver)
        time.sleep(5)
        select_emp.select_employees()  # Precondición --> Haber generado X cantidad de empleados
        select_emp.generate()
        docs.print()
        time.sleep(5)
        docs.check_print()
        # Example:
        # def test_ispath(small_image, compression):
        # assert os.path.exists(small_image)
