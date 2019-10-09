import time
from selenium import webdriver
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\admin\\Downloads\\chromedriver.exe")
        cls.driver.maximize_window()


    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    #UserName
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")

    #Password
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")

    #Login Button
        self.driver.find_element_by_id("btnLogin").click()

    #Home Page
        self.driver.find_element_by_id("welcome").click()

        self.time.sleep(5)

    #Logout
        self.driver.find_element_by_link_text("Logout").click()

    @classmethod
    def tearDown(cls):

        cls.time.sleep(2)
        cls.driver.quit()

print("Test complete")

