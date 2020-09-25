from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Booking_Test():
    def open_url(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        baseUrl = "https://www.booking.com"
        driver.maximize_window()
        driver.get(baseUrl)

        #Select Flights

        flight = driver.find_element_by_xpath("//a[@class='xpb__link']//span[text()='Flights']")
        flight.click()

        #From City

        frommCity = driver.find_element_by_xpath("//div[@id='wo9e-origin-airport-display']")
        frommCity.click()
        frommCity.send_keys("Delhi")





bk = Booking_Test()
bk.open_url()