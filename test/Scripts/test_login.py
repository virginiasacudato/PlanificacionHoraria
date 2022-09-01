import time

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")


class Test_login(WebDriverSetup):

    def test_login(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        time.sleep(3)
        home_page.login(USER, PASSWORD)
        home_page.click_login()
        time.sleep(7)
        home_page.plan_horaria()
        time.sleep(5)
