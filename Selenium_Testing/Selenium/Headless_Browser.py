from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.chrome()

driver.get("http://www.python.org")

assert "Python" in driver.title

ele = driver.find_element_by_name("q")