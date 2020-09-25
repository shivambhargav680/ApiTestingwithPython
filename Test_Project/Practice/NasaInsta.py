from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.instagram.com/nasa/?hl=en")


ele = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div[1]/div[2]")
print(ele.get_attribute("innerHTML")) 