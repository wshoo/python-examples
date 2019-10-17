import time
import json
import redis
from selenium import webdriver

client = redis.StrictRedis()

driver = webdriver.Chrome('./chromedrive')
drive = get('http://exercise.kingname.info/exercise_login_success')

user = driver.find_element_by_xpath("//input[@name='username']")
user.clear()
user.send_keys('name')

password = driver.find_element_by_xpath("//input[@name='password']")
password.clear()
password.send_keys('password')

remember = driver.find_element_by_xpath("//botton[@name='remember']")
remember.click()

login = drive.find_element_by_xpath("//botton[@class='login']")
login.click()

time.sleep(2)
cookies = drive.get_cookies()

client.lpush('cookies', json.dumps(cookies))
drive.quit()







 