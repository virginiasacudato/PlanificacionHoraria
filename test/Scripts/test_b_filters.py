import time
from src.TestBase.WebDriverSetup import WebDriverSetup
import os
from src.PageObject.Pages.Filters import Filters
from src.PageObject.Pages.PreconditionSQL import *
from src.PageObject.Pages.PlanificacionHoraria import PlanificacionHoraria


#class Test_filters(WebDriverSetup):
#
#    def test_a_select_date(self):
#        condition_sql()
#        driver = self.driver
#        filters = Filters(driver)
#        select_emp = PlanificacionHoraria(driver)
#        filters.select_date()
#        time.sleep(5)
#        select_emp.select_employees()
#        select_emp.generate()
#        filters.check_filter_date()
#
#
#    def test_b_checkbox(self):
#        driver = self.driver
#        filters = Filters(driver)
#        select_emp = PlanificacionHoraria(driver)
#        time.sleep(9)
#        select_emp.select_employees()
#        select_emp.generate()
#        time.sleep(4)
#        filters.checkbox_sun_sat()
#        time.sleep(6)
#        delete_sql()






