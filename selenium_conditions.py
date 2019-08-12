from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

driver.get("http://www.google.com")

search_field = driver.find_element_by_name("q")

if search_field.is_displayed():
    search_field.send_keys("Python")

driver.close()