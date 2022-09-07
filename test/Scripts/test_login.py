import time

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage
from src.PageObject.Pages.PlanificacionHoraria import PlanificacionHoraria
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")


# Run -->  python -m pytest
# Run with messages console --> python -m pytest -s


class Test_login(WebDriverSetup):

    def test_a_login(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        time.sleep(3)
        home_page.login("admin", "admin")
        home_page.click_login()

    def test_b_select_employ(self):
        global plan_horaria
        driver = self.driver
        self.driver.get(PlanificacionHoraria.get_base_url())
        plan_horaria = PlanificacionHoraria(driver)
        self.test_a_login()
        time.sleep(9)
        plan_horaria.plan_horaria()
        time.sleep(5)
        plan_horaria.select_employees()
        plan_horaria.generate()
        plan_horaria.check_emp_gen()

    def test_c_mod_jornada_com(self):
        self.test_b_select_employ()
        plan_horaria.mod_fulltime_employee()
        time.sleep(8)
        plan_horaria.save_changes()

    def test_d_mod_jor_parc(self):
        self.test_b_select_employ()
        plan_horaria.mod_spec_days()






