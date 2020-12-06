from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class MMT_Test():
    def open_url(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\\Downloads\\Testing\\Selenium\\chromedriver.exe")
        baseUrl = "https://www.makemytrip.com"
        driver.maximize_window()
        driver.get(baseUrl)

        #From City

        from_city = driver.find_element_by_xpath("//input[@id='fromCity']")
        from_city.send_keys("Delhi")
        time.sleep(2)

        #To City

        to_city = driver.find_element_by_css_selector("#toCity")
        to_city.send_keys("Mumbai")
        time.sleep(2)

        #Departure
        departure = driver.find_element_by_xpath("//div[@class='fsw_inputBox dates inactiveWidget ']")
        departure.click()

        #Ad Disable
        ad = driver.find_element_by_xpath("//span[@class='ic_circularclose_grey']").click()

        #Select Date
        select_date = driver.find_element_by_xpath("//div[@class='DayPicker-Month'][position()=1]//div[@aria-label='Tue Nov 30 2020']").click()

        #Search Result
        Srch = driver.find_element_by_xpath("//a[text()='Search']").click()

mmt = MMT_Test()
mmt.open_url()
