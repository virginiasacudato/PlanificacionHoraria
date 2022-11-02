import time
import pytest

from src.PageObject.Pages.PreconditionSQL import *
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.PlanificacionHoraria import PlanificacionHoraria


# Run -->  python -m pytest
# Run with messages console --> python -m pytest -s

class Test_login(WebDriverSetup):

     def test_a_mod_jornada_com(self):
        condition_sql()
        driver = self.driver
        plan_horaria = PlanificacionHoraria(driver)
        plan_horaria.select_employees()
        plan_horaria.generate()
        plan_horaria.mod_fulltime_employee()
        plan_horaria.save_changes()
        delete_sql()



