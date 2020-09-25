import time
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\admin\\Downloads\\chromedriver.exe")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

#UserName
driver.find_element_by_id("txtUsername").send_keys("Admin")

#Password
driver.find_element_by_id("txtPassword").send_keys("admin123")

#Login Button
driver.find_element_by_id("btnLogin").click()

#Home Page
driver.find_element_by_id("welcome").click()

time.sleep(5)

#Logout
driver.find_element_by_link_text("Logout").click()

time.sleep(2)

driver.close()

print("Test complete")

















































'''
class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))



def Widget(param):
    pass


class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The Widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(),(50,50),"incorrect default size")

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(),(100,150),"wrong size after resize")

    def tearDown(self):
        self.widget.dispose()'''




