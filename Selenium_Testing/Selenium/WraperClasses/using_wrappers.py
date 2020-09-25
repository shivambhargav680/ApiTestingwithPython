from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium_Testing.Selenium.WraperClasses.Wraperclass import Handywrapper
import time


class openbrowser():
    def test(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        baseUrl = "https://www.makemytrip.com"
        driver.maximize_window()
        HW = Handywrapper(driver)
        driver.get(baseUrl)

        # From City

        from_city =HW.getElement("fromCity")
        from_city.send_keys("Delhi")
        time.sleep(2)

        # To City

        to_city = HW.getElement("#toCity","css_selector")
        to_city.send_keys("pune")
        time.sleep(2)

cd = openbrowser()
cd.test()