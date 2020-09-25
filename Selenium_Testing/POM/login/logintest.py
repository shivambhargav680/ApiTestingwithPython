from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class logintest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()


    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a").click()
        time.sleep(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
