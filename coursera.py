from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
import time
import pyautogui as pg


email = 'piyushagarwal.0108@gmail.com'
print("Enter your password: ")
password = 'qwerty12345'

course = 'Python for Everybody'
cookie_file = open('cookies.txt')
cookie = cookie_file.read()

options = Options()
options.add_extension("/usr/bin/extension_1_5_0_0.crx")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)  # opens the chrome browser
#driver = webdriver.Chrome(options=options)
def coursera():
    # opens google chrome
    #driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")  # opens the chrome browser
    driver.maximize_window()
    # a timer for all the commands to keep things smooth
    driver.implicitly_wait(10)
    # open coursera 
    driver.get("https://www.coursera.org")  # opens the webpage
    time.sleep(120)
    
    print("time to add cookie")
    # Add coursera cookie
    pg.click(1797,131)  # select cookie extension
    time.sleep(1)
    pg.click(1554,117) # select import cookie button
    time.sleep(1)
    pg.click(1404,245) # click on text input field
    time.sleep(1)
    pg.typewrite(cookie)  # enter coursera cookies
    time.sleep(1)
    pg.click(1547,687)  # save the cookies

    time.sleep(8)
    # now refresh the page 
    driver.refresh()

    # open coursera 
    # driver.get("https://www.coursera.org")  # opens the webpage

    print("Opened the Webpage:",driver.title,"with url: ",driver.current_url)

coursera()

# Code to find a course
wait = WebDriverWait(driver,10)

course_field = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rendered-content"]/div/div/span/div[2]/header/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/div/div[1]/div/input')))
course_field.clear().send_keys(course) # types in the course
time.sleep(3)
driver.find_element_by_xpath('//*[@id="rendered-content"]/div/div/span/div[2]/header/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/div/div[1]/button[2]/div').click()

time.sleep(10)
# time to select the course





