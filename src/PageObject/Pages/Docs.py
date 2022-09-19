from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Docs:

    def __init__(self, driver):
        # Locators
        self.driver = driver
        self.print_btn = 'printBtn'
        self.img = 'image'
        self.print_win = '/html/body/print-preview-app'

    # Get Elements
    def get_print_btn(self):
        return self.driver.find_element(By.ID, self.print_btn)

    def get_img(self):
        return self.driver.find_element(By.ID, self.img)

    def get_print_win(self):
        return self.driver.find_element(By.XPATH, self.print_win)

    # Actions
    def print(self):
        self.get_print_btn().click()

    def check_print(self):
        # Cambiar de pestaña
        # self.driver.switch_to.window(self.driver.window_handles[1])
        if self.get_print_win():
            print("Archivo generado!")
        else:
            NoSuchElementException()
