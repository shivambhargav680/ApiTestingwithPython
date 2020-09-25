from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

chrome_option = webdriver.ChromeOptions();
chrome_option.add_experimental_option("excludeSwitches",['enable-automation']);

driver = webdriver.Chrome("C:\\Users\\admin\\Downloads\\chromedriver.exe")

#Open URL
driver.get("https://www.redbus.in")
time.sleep(5)

#Source Element
driver.find_element_by_id("src").send_keys("delhi")
time.sleep(3)
driver.find_element_by_xpath("//ul[@class='autoFill']//li[@data-no='1']").click()

#Destination Element
driver.find_element_by_id("dest").send_keys("jaipur")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/div/ul/li[1]").click()

#Onward Date
driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']/table[@class='rb-monthTable first last']/tbody/tr[7]/td[4]").click()

#Return Date
#driver.find_element_by_id("return_cal")

#driver.find_element_by_xpath("//div[@id='rb-calendar_return_cal']/table[@class='rb-monthTable first last']/tbody/tr[7]/td[6]").click()

# Search
driver.find_element_by_id("search_btn").click()
time.sleep(5)

lst_bus = driver.find_element_by_xpath("//div[@class='result-sec']")

for i in lst_bus:
    print(i.text)
#driver.find_element_by_xpath("//*[@id='9758487']/div/div[2]/div[1]").click()
time.sleep(3)

#seat_list = driver.find_elements_by_xpath("//canvas[@data-type='lower']")

#for emp_seat in range(seat_list):
#    print(emp_seat.__getattribute__("innerHTML"))