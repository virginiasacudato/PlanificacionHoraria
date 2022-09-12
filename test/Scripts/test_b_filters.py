import time
from src.TestBase.WebDriverSetup import WebDriverSetup
import os
from src.PageObject.Pages.Filters import Filters


class Test_filters(WebDriverSetup):

    def test_a_select_emp_sec(self):
        driver = self.driver
        filters = Filters(driver)
        filters.select_emp_sec()

    def test_b_select_date(self):
        driver = self.driver
        filters = Filters(driver)
        filters.select_date()
        time.sleep(15)
        filters.check_filter_date()


