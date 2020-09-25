from selenium import webdriver
from selenium.webdriver.common.by import By
class path_setup():
    def test(self):
        base_url = "https://in.yahoo.com"
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        driver.get(base_url)
        ele_xpath = driver.find_elements_by_xpath("")

        if ele_xpath is not None:
            print("We found element by xpath")

        ele_css = driver.find_element_by_css_selector("")

        if ele_css is not None:
            print("We found element by css selector")

ch=path_setup()
ch.test()
