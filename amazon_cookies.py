from selenium import webdriver
import csv
from time import sleep


driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get('https://amazon.com')


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
