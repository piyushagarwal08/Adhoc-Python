from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time
import pyautogui as pg
from selenium.webdriver.support.ui import Select


#email = input('Please enter your email: ')
#password = input('Please enter your password: ')

course = 'Object Oriented Programming in Java Specialization'   # pls enter your course name
cookie_file = open('cookies.txt')  # account cookies should be saved with same name
cookie = cookie_file.read()
cookie_file.close()

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
    time.sleep(3)
    
    print("time to add cookie")
    # Add coursera cookie
    pg.click(1819,94)  # select cookie extension
    time.sleep(1)
    pg.click(1542,112) # select import cookie button
    time.sleep(1)
    pg.click(1441,283) # click on text input field
    time.sleep(1)
    pg.typewrite(cookie)  # enter coursera cookies
    time.sleep(1)
    pg.click(1544,693)  # save the cookies

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
    pg.click(462,266) # selects the course
    driver.find_element_by_id('finaid_button').click()  # click on financial update available
    time.sleep(1)
    driver.find_element_by_id('financial_aid_modal_apply_button').click()  # continue to financial aid
    wait = WebDriverWait(driver,20)
    time.sleep(8)
    print('time to open actual application')
    #pg.click(570,684)  # click on first check box
    driver.find_element_by_id('info_checkbox').click()  # click on 1st checkbox
    driver.find_element_by_id('completion_checkbox').click() # click on 2nd checkbox  
    time.sleep(1)

    driver.find_element_by_id('accept-terms-field').send_keys('I agree to the terms above') # enter agree terms in text field
    time.sleep(1)

    application_button = wait.until(EC.element_to_be_clickable((By.ID,'continue_finaid_application_button')))
    application_button.click() # clicks on application continue button

    education = Select(driver.find_element_by_id('finaid-educationalBackground')) # instance of educational background
    education.select_by_value('SOME_COLLEGE')  # select some college 
    print(type(education))

    time.sleep(1)
    annual_income = driver.find_element_by_id('finaid-income')
    annual_income.clear()
    annual_income.send_keys('1023')  # enter in the field of annual income

    time.sleep(1)
    employment = Select(driver.find_element_by_id('finaid-employmentStatus'))  # instance of employment status
    employment.select_by_value('STUDENT') # select student as status

    time.sleep(1)
    payable = driver.find_element_by_id('finaid-amount-can-pay')   # possible amount we can pay set to 0
    payable.clear()
    payable.send_keys('0')

    time.sleep(1)
    file1 = open('para1')
    para1 = file1.read()
    driver.find_element_by_id('finaid-reason').send_keys(para1)  # first paragraph filled successfully
    file1.close()

    time.sleep(1)
    file2 = open('para2')
    para2 = file2.read()
    driver.find_element_by_id('finaid-goal').send_keys(para2)    # second paragraph filled
    file2.close()

    time.sleep(1)
    driver.find_element_by_id('finaid-loanReason').send_keys('Currently i have no source of income')  # third paragraph filled

    print('Filled the finally form also successfully')
    # finally to submit application
    driver.find_element_by_id('submit_application_button').click()
    time.sleep(8)
    driver.quit()

coursera()

