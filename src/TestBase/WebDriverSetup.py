import unittest
from selenium import webdriver
import urllib3


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
