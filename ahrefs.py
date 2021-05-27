from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://ahrefs.com/dashboard")

username_box = browser.find_element_by_name("email")
username_box.send_keys("brigham.h@alder.com")

password_box = browser.find_element_by_name("password")
password_box.send_keys("98thFloor")
password_box.submit()
time.sleep(10)

cove_data = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/div/div/h3/div/a")
cove_data.click()
time.sleep(5)

export_csv = browser.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div/ul/li[13]/ul/li[1]/a")
export_csv.click()
time.sleep(5)

download_backlinks = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[1]/div/form/div[5]/div[2]/input')
download_backlinks.click()
time.sleep(90)

download_file = browser.find_element_by_xpath('/html/body/div[1]/nav[1]/ul/li[1]/div[1]/div/div[3]/a[1]/div/span[1]/span')
download_file.click()
time.sleep(10)

browser.close()