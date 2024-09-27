from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
from time import sleep


chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com')


with open('amazon_cookies.csv', 'r') as file:
    data = csv.DictReader(file)
    cookies = list(data)
    # print(cookies)

for cookie in cookies:
  #  driver.add_cookie(cookie)
  # Ensure the cookie format is correct
    cookie_dict = {
        'name': cookie['name'],
        'value': cookie['value'],
        'domain': cookie['domain'],
        'path': cookie['path'],
        'expires': int(cookie['expires']),  # Convert to int if needed
        'secure': cookie['secure'].lower() == 'true',  # Convert to boolean
        'httpOnly': cookie['httpOnly'].lower() == 'true',  # Convert to boolean
    }
    driver.add_cookie(cookie_dict)

sleep(5) # Wait for a bit before refreshing
driver.refresh()

print(driver.get_cookies()) # Print the current cookies

driver.close() # Close the browser
