from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys
itemidurl = "the whole url of the item you want to bid on"
maxbidebay = "you max bid amount with no doolar sign example 1.50"
timetobidmins = 5 # change this to the time in mins to bid
sedbid = timetobidmins * 60
print sedbid
time.sleep(sedbid)
driver = webdriver.Firefox()
driver.get('https://www.ebay.com')
time.sleep(3)
io = driver.find_element_by_link_text('Sign in')
io.click()
time.sleep(3)
elements = driver.find_elements_by_class_name("fld")
elements[2].send_keys("your ebay username")
elements[3].send_keys("your ebay password")
button = driver.find_element_by_id("sgnBt")
button.click()
time.sleep(2)
driver.get(itemidurl)
time.sleep(3)
elements = driver.find_element_by_id("MaxBidId")
elements.send_keys(maxbidebay)
elements = driver.find_element_by_id("bidBtn_btn")
elements.click()
time.sleep(3)
io = driver.find_element_by_css_selector("a[id*='reviewBidSec_btn']")
io.click()
time.sleep(20)
driver.quit()