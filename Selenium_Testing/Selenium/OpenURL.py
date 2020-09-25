from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class Starting():
    def test(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)

        ele = driver.find_element_by_id("carselect")
        sel = Select(ele)
        sel.select_by_index("2")
        print("Honda is selected")
        time.sleep(2)

        sel.select_by_value("bmw")
        print("BMW is selected")
        time.sleep(2)

        sel.select_by_visible_text("Benz")


cd = Starting()
cd.test()