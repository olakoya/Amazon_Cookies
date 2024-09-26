from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
from time import sleep


chrome_driver_path = "/Users/olakoya/Bin/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com')


with open('amazon_cookies.csv', 'r') as file:
    data = csv.DictReader(file)
    cookies = list(data)
    # print(cookies)

for cookie in cookies:
    driver.add_cookie(cookie)
sleep(5)
driver.refresh()

print(driver.get_cookies())

driver.close()
