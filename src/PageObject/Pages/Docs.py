from selenium.webdriver.common.by import By
import random
import time
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Filters:

    def __init__(self, driver):
        # Locators
        self.driver = driver


