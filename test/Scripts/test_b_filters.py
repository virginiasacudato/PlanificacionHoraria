import time
from src.TestBase.WebDriverSetup import WebDriverSetup
import os
from src.PageObject.Pages.Filters import Filters
from src.PageObject.Pages.PlanificacionHoraria import PlanificacionHoraria


class Test_filters(WebDriverSetup):

    def test_a_select_emp_sec(self):
        driver = self.driver
        filters = Filters(driver)
        filters.select_emp_sec()

    def test_b_select_date(self):
        driver = self.driver
        filters = Filters(driver)
        select_emp = PlanificacionHoraria(driver)
        filters.select_date()
        time.sleep(5)
        select_emp.select_employees()
        select_emp.generate()
        filters.check_filter_date()





