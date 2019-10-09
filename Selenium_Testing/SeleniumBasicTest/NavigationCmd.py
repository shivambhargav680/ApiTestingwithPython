from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")

print(driver.title)

driver.get("https://www.skyscanner.co.in/")

print(driver.title)

driver.back()

#print(driver.title)

#driver.forward()

print(driver.title)

time.sleep(5)

driver.close()
