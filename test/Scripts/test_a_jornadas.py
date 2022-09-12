import time
import pytest

# from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
# from src.PageObject.Pages.HomePage import HomePage
from src.PageObject.Pages.PlanificacionHoraria import PlanificacionHoraria

# Run -->  python -m pytest
# Run with messages console --> python -m pytest -s

# REFACTORIZAR MENSAJES DE CONSOLA
# REFACTORIZAR save_changes --> asserts¿?


class Test_login(WebDriverSetup):
    @pytest.mark.dependency()
    def test_a_select_employ(self):
        global plan_horaria
        driver = self.driver
        plan_horaria = PlanificacionHoraria(driver)
        plan_horaria.select_employees()
        plan_horaria.generate()
        plan_horaria.check_emp_gen()

    @pytest.mark.dependency(depends=["test_a_select_employ"])
    def test_b_mod_jornada_com(self):
        self.test_a_select_employ()
        plan_horaria.mod_fulltime_employee()
        plan_horaria.save_changes()

    @pytest.mark.dependency(depends=["test_a_select_employ"])
    def test_c_mod_jor_parc(self):
        self.test_a_select_employ()
        plan_horaria.mod_spec_days()
        plan_horaria.save_changes()
