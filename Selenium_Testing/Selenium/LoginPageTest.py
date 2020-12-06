from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import xlrd

"""
driver =webdriver.Chrome()
driver.get("https://andrew.hedges.name/experiments/haversine/")

driver.find_element(By.XPATH, '//input[@name="lat1"]').clear()
driver.find_element(By.XPATH, '//input[@name="lon1"]').clear()
driver.find_element(By.XPATH, '//input[@name="lat2"]').clear()
driver.find_element(By.XPATH, '//input[@name="lon2"]').clear()

driver.implicitly_wait(time_to_wait=5)
driver.find_element(By.XPATH, '//input[@name="lat1"]').send_keys("19.9905379")
driver.find_element(By.XPATH, '//input[@name="lon1"]').send_keys("73.7325622")
driver.find_element(By.XPATH, '//input[@name="lat2"]').send_keys("19.9669174")
driver.find_element(By.XPATH, '//input[@name="lon2"]').send_keys("73.7659002")

driver.find_element(By.XPATH, '//input[@type="submit"][@value="Calculate"]').click()

dis = driver.find_element(By.XPATH, '//input[@type="text"][@name="km"]')
dis1=dis.get_attribute('value')
print(dis1)
"""
path = ("C:\\Users\\admin\Desktop\Attendance_location_Data\TestLocations.xlsx")
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)
sheet.cell_value(0,0)
#print(sheet.nrows)
#print(sheet.ncols)

"""for j in range(sheet.nrows):
   lat = sheet.cell_value(j,2)
   list=[lat]
   print(list)


for i in range(sheet.nrows):
    lng = sheet.cell_value(i,3)
   # print(lng)
"""
"""l=[]
for i in range (2000,3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(l)
"""

x=8
def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)
x=int(raw_input())
print (fact(x))