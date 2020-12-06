from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# Open url
driver.get("https://agrichain.com/qa/input")
# Find input text box and send value
driver.find_element_by_id("input_txt").send_keys("abcabcbb")
# Click on submit button
driver.find_element_by_id("submit_btn").click()
# Click back to home button
driver.find_element_by_id("backtohome_btn").click()

# Close the current browser window
driver.close()