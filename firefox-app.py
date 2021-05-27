from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
# browser.get("https://dsm.commercehub.com/dsm/gotoHome.do")
browser.get("https://dsm.commercehub.com/dsm/gotoOrderSearch.do")

username_box = browser.find_element_by_id("username")
username_box.send_keys("austin.c")

password_box = browser.find_element_by_id("password")
password_box.send_keys("98thFloor!")
password_box.submit()



browser.close()