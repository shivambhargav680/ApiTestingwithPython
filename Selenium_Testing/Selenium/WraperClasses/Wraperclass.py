from selenium import webdriver
from selenium.webdriver.common.by import By

class Handywrapper():
    def __init__(self,driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css_selector":
            return By.CSS_SELECTOR
        else:
            print("Wrong type")
        return False

    def getElement(self, locator, locatoType = 'id'):
        element = None
        try:
            locatoType = locatoType.lower()
            byType = self.getByType(locatoType)
            element = self.driver.find_element(byType, locator)
            print("element found")
        except:
            print("Not found")
        return element
