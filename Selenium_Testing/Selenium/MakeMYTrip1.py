from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class MMT_Test():
    def open_url(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        baseUrl = "https://www.makemytrip.com"
        driver.maximize_window()
        driver.get(baseUrl)

        #From City

        from_city = driver.find_element_by_xpath("//input[@id='fromCity']")
        from_city.send_keys("Delhi")
        time.sleep(2)

        #To City

        to_city = driver.find_element_by_css_selector("#toCity")
        to_city.send_keys("pune")
        time.sleep(2)

        #Departure
        #departure = driver.find_element_by_css_selector("#departure")
        #departure.send_keys("10-Aug-2020")

        #driver.find_element_by_xpath("//div[@class='DayPicker-Day DayPicker-Day--selected']//p[text()='10']").click()

        #Click on Search Button
        search_btn = driver.find_element_by_xpath("//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']")
        search_btn.click()


mmt = MMT_Test()
mmt.open_url()
