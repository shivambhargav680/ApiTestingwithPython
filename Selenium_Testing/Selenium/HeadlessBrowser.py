from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import time


"""chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome'"""


#driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\\Downloads\\Testing\\Selenium\\chromedriver.exe")
driver.get("https://www.redbus.in")

time.sleep(10)

alrt_obj = driver.switch_to_alert().text("block")

driver.find_element_by_id("src").send_keys("delhi")
