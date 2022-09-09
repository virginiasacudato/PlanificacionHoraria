import time
from src.TestBase.WebDriverSetup import WebDriverSetup
import os
from test.Scripts.test_a_jornadas import Test_login
from src.PageObject.Pages.Filters import Filters


class Test_filters(WebDriverSetup):

    def test_a_select_emp_sec(self):
        driver = self.driver
        filters = Filters(driver)
        filters.select_emp_sec()

