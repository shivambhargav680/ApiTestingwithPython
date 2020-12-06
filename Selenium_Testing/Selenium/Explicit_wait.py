from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class ex_wait():

    def test(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\\Downloads\\Testing\\Selenium\\chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://www.expedia.co.in/?pwaLob=wizard-hotel-pwa-v2")

        #Select flight tag
        driver.find_element_by_xpath("//li[@class='uitk-tab uitk-tab-icon-text  active']//a").click()
        driver.find_element_by_id("d1-btn").send_keys("16/09/2020")


ex = ex_wait()
ex.test()
