from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://apps.commercehub.com/account/login?service=https://dsm.commercehub.com/dsm/shiro-cas")

username_box = browser.find_element_by_id("username")
username_box.send_keys("austin.c")

password_box = browser.find_element_by_id("password")
password_box.send_keys("98thFloor!")
password_box.submit()