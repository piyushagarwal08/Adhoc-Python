from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
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
    driver.maximize_window()
    # a timer for all the commands to keep things smooth
    driver.implicitly_wait(10)
    # open coursera 
    driver.get("https://www.coursera.org")  # opens the webpage
    time.sleep(7)
    
    print("time to add cookie")
    # Add coursera cookie
    pg.click(1797,119)  # select cookie extension
    time.sleep(1)
    pg.click(1416,144) # select import cookie button
    time.sleep(1)
    pg.click(1289,316) # click on text input field
    time.sleep(1)
    pg.typewrite(cookie)  # enter coursera cookies
    time.sleep(1)
    pg.click(1424,894)  # save the cookies

    time.sleep(3)
    # now refresh the page 
    driver.refresh()

    print("Opened the Webpage:",driver.title,"with url: ",driver.current_url)
    # Code to find a course
    wait = WebDriverWait(driver,10)

    course_field = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rendered-content"]/div/div/span/div[2]/header/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/div/div[1]/div/input')))
    course_field.clear()
    course_field.send_keys(course) # types in the course
    time.sleep(3)
    print('time to select the course')
    pg.click(629,335) # selects the course
    driver.find_element_by_id('finaid_button').click()  # click on financial update available
    time.sleep(1)
    driver.find_element_by_id('financial_aid_modal_apply_button').click()  # continue to financial aid

coursera()

wait = WebDriverWait(driver,20)
time.sleep(8)
#pg.click(570,684)  # click on first check box
driver.find_element_by_id('info_checkbox').click()  # click on 1st checkbox
driver.find_element_by_id('completion_checkbox').click() # click on 2nd checkbox  
time.sleep(1)

driver.find_element_by_id('accept-terms-field').send_keys('I agree to the terms above') # enter agree terms in text field
time.sleep(1)

application_button = wait.until(EC.element_to_be_clickable((By.ID,'continue_finaid_application_button')))
application_button.click() # clicks on application continue button

