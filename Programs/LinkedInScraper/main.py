from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from parsel import Selector
import parameters
import functions
import time

service = Service('D:\Skills\Repos\Python\Google Meet Bot\ChromeDrivers\win32\chromedriver')
driver = webdriver.Chrome(service = service)
driver.get('https://www.linkedin.com')
driver.maximize_window()

sign_in_button = driver.find_element_by_xpath('/html/body/nav/div/a[2]')
sign_in_button.click()
time.sleep(3)

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys(parameters.linkedin_username)
time.sleep(0.5)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(parameters.linkedin_password)
time.sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
time.sleep(5)

driver.get('https:www.google.com')
time.sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
time.sleep(0.5)

search_query.send_keys(Keys.RETURN)
time.sleep(5)

linkedin_url = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a').get_attribute('href')
driver.get(linkedin_url)
time.sleep(10)

start = time.time()
 
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
 
while True:
    driver.execute_script(f'window.scrollTo({initialScroll},{finalScroll})')
    
    initialScroll = finalScroll
    finalScroll += 1000
    time.sleep(3)
 
    end = time.time()
 
    if round(end - start) > 20:
        break

sel = Selector(text=driver.page_source)

name = sel.xpath('//*[@id="ember30"]/div[2]/div[2]/div[1]/div[1]/h1/text()').get()
if name :
    name = name.strip()

tagline = sel.xpath('//*[@id="ember30"]/div[2]/div[2]/div[1]/div[2]/text()').get()
if tagline :
    tagline = tagline.strip()

interests = sel.xpath('//*[@id="ember30"]/div[2]/div[2]/div[1]/div[3]/span[1]/text()').get()
if interests :
    interests = interests.strip()
    
company = sel.xpath('//*[@id="ember30"]/div[2]/div[2]/ul/li/button/span/div/text()').get()
if company :
    company = company.strip()

college = sel.xpath('//*[@id="ember659"]/div[2]/div[2]/ul/li[2]/button/span/div/text()').get()
if college :
    college = college.strip()

location = sel.xpath('//*[@id="ember30"]/div[2]/div[2]/div[2]/span[1]/text()').get()
if location :
    location = location.strip()

read_more_btn = driver.find_element_by_xpath('//*[@id="ember67"]/div[3]/div/div')
read_more_btn.click()
time.sleep(2)
sel = Selector(text=driver.page_source)

about_parts = sel.xpath('//*[@id="ember105"]/div[3]/div/div/div/span[1]/text()').getall()
print(about_parts)
about = ""
for i in about_parts :
    about += i
if about :
    about = about.strip()

name = functions.validate_field(name)
about = functions.validate_field(about)
tagline = functions.validate_field(tagline)
company = functions.validate_field(company)
college = functions.validate_field(college)
location = functions.validate_field(location)
linkedin_url = functions.validate_field(linkedin_url)

print('\n')
print(f'Name : {name}')
print(f'About : {about}')
print(f'Tagline : {tagline}')
print(f'Interests : {interests}')
print(f'Company : {company}')
print(f'College : {college}')
print(f'Location : {location}')
print(f'URL : {linkedin_url}')
print('\n')

driver.quit()