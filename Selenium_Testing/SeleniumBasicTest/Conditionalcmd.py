from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
#driver.find_element_by_id("email").send_keys("shivam")
#driver.find_element_by_xpath("//input[@id='pass']").send_keys("shivam")

emailtxt = driver.find_element_by_id("email")
print(emailtxt.is_displayed())
print(emailtxt.is_enabled())
emailtxt.send_keys("shivam")

passtxt = driver.find_element_by_xpath("//input[@id='pass']")
print(passtxt.is_displayed())
print(passtxt.is_enabled())
passtxt.send_keys("shivam")

driver.find_element_by_xpath("//input[@value='Log In']").click()


"""def email():
    if emailtxt.is_displayed():
        print("Email textbox is displayed")
    else:
        print("Email textbox is not displayed")


def password():
    if passtxt.is_displayed():
        print("Pass textbox is displayed")
    else:
        print("Password is not displayed")


print(email())
print(password())"""