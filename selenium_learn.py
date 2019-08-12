from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("https://www.coursera.org")

print(driver.title)  # title of the page

print(driver.current_url)  # returns the current page url

driver.get("https://www.google.com")
#print(driver.page_source)  # returns the HTML code of the page opened

#driver.find_element_by_xpath('//*[@id="c-ph-right-nav"]/ul/li[4]/a').click()
driver.back()  # switch web-url to single page backward

driver.close()   # close the browser