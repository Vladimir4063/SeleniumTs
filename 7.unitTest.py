import unittest
from selenium import webdriver
import time

class newTours(unittest.TestCase):
    def setUp(self): # espacio de trabajo
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://blazedemo.com')
        time.sleep(4)

    def test_dropdown(self):

    def close(self):
        self.driver.quit()
