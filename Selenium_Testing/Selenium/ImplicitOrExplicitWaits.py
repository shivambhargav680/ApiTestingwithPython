from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/") # opening URL takes some time

driver.implicitly_wait(10) #Sec

assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" in driver.title

def mousehover():
    action = ActionChains(driver)

    firstele = driver.find_element_by_xpath("//*[@id='nav-link-yourAccount']")
    action.move_to_element(firstele).perform()
    driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span").click()

print(mousehover())

driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='continue']").click()

