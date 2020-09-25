from selenium import webdriver

class path_setup():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        driver.get(base_url)
        ele_id = driver.find_elements_by_id("name")

        if ele_id is not None:
            print("id is not present")


ch=path_setup()
ch.test()
