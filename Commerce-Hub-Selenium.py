from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get("https://dsm.commercehub.com/dsm/gotoHome.do")
# browser.get("https://dsm.commercehub.com/dsm/gotoOrderSearch.do")

username_box = browser.find_element_by_id("username")
username_box.send_keys("austin.c")

password_box = browser.find_element_by_id("password")
password_box.send_keys("98thFloor!")
password_box.submit()

time.sleep(15)

button = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/ol/li[1]/ol/li[3]/a')
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(button).click(button).perform()


