from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import *
from selenium.webdriver.common.by import By

YOUR_PATH=""
USERNAME=""
PASSWORD=""
URL=""

service=Service(executable_path="D:\Skills\Python\Projects\Google Meet Bot\ChromeDrivers\win32\chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get(URL)
sleep(3)
signin=driver.find_element_by_link_text('Sign in')
signin.click()
sleep(3)
username=driver.find_element_by_id('username')
username.send_keys(USERNAME)
password=driver.find_element_by_id('password')
password.send_keys(PASSWORD)
signinbtn=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
signinbtn.click()
sleep(10)
allis=driver.find_elements_by_css_selector('.scaffold-layout__list-item')
print(allis)
for li in allis:
    li.click()
    savebtn=driver.find_element_by_css_selector('.artdeco-button--3, .artdeco-button--4')
    savebtn.click()
    driver.implicitly_wait(10) 
driver.quit()