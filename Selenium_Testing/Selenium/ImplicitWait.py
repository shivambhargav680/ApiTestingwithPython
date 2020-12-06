from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class IM_Wait():
    def test(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\\Downloads\\Testing\\Selenium\\chromedriver.exe")
        driver.get("https://www.expedia.co.in/?pwaLob=wizard-hotel-pwa-v2")
        driver.maximize_window()

        # Select flight tag
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//button[@aria-label='Going to']").click()
        #driver.find_element_by_xpath("//li[@class='uitk-tab uitk-tab-icon-text  active']//a").click()
        #driver.find_element_by_id("d1-btn").send_keys("16/09/2020")


imwait = IM_Wait()
imwait.test()