from selenium import webdriver

class yahoosignin():
    def test(self):
        baseurl= "https://in.yahoo.com"
        driver = webdriver.Chrome("C:\\Users\\Hitesh bhargav\Downloads\Testing\Selenium\chromedriver.exe")
        driver.get(baseurl)
        driver.find_element_by_css_selector("#header-signin-link").click()


yt= yahoosignin()
yt.test()