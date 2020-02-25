from selenium import webdriver
import time
import logindata

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('F:\Channel\webdriver\chromedriver.exe', chrome_options=options)
time.sleep(1)

driver.get('http://www.github.com')
time.sleep(3)

continue_link = driver.find_element_by_link_text('Sign in')
continue_link.click()
time.sleep(3)
if driver.find_element_by_name('login'):
    pass
else:
    time.sleep(2)
    
login = driver.find_element_by_name('login')
password = driver.find_element_by_name("password")
time.sleep(0.5)
    
login.send_keys(logindata.USERNAME)
time.sleep(1)
    
password.send_keys(logindata.PASSWORD)
time.sleep(1)
    
button = driver.find_element_by_name('commit')
button.click()
time.sleep(2)
