import unittest
from selenium import webdriver
import urllib3
from selenium.webdriver.common.by import By
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/PlanificacionHoraria/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

BASE_URL = os.getenv('URL')


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(BASE_URL)
        self.driver.find_element(By.ID, 'Usuario').send_keys(USER)
        self.driver.find_element(By.ID, 'Password').send_keys(PASSWORD)
        self.driver.find_element(By.ID, 'btnIngresar').click()
        self.driver.find_element(By.XPATH, '/html/body/main/aside/section/nav/ul/li[3]/div/label').click()
        self.driver.find_element(By.XPATH, '/html/body/main/aside/section/nav/ul/li[3]/div/div/ul/li[3]/a').click()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
