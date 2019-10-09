from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver.get("http://www.google.com")
driver.get("https://in.yahoo.com")
tlt = "Google"

tlt1 = driver.title

def pagetitle():
    if tlt1==tlt:
        print("Title Matched")
    else:
        print("Title is not matched")

print(pagetitle())

def pageclose():
    driver.close()
print(pageclose())