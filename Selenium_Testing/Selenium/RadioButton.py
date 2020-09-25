from selenium import webdriver

class RadioBtn():
    def test(self):
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)

        ele = driver.find_elements_by_xpath("//input[@type='radio']")
        size = len(ele)

        print("Size of the list" + str(size))
        for txt in ele:
            isSelected = txt.is_selected()
            if not isSelected:
                txt.click()


rb=RadioBtn()
rb.test()