from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
from time import sleep


# chrome_driver_path = "/usr/local/bin/chromedriver"
# ChromeDriverManager = "/usr/local/bin/chromedriver"

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to Amazon
driver.get('https://www.amazon.com')

# Load cookies from CSV and add them to the browser
with open('amazon_cookies.csv', 'r') as file:
    data = csv.DictReader(file)
    cookies = list(data)
    # print(cookies)

for cookie in cookies:
   # driver.add_cookie(cookie)

  # Ensure the cookie format is correct
    cookie_dict = {
        'name': cookie['name'],
        'value': cookie['value'],
        'domain': cookie.get('Domain', '.amazon.com'), # Default to '.amazon.com' if missing
        'path': cookie.get('path', '/'), # Default to '/' if missing
        'expires': int(cookie.get('expires', 0)),  # Convert to int if needed & Default to 0 if missing
        'secure': cookie.get('secure', 'false').lower() == 'true',  # Convert to boolean & Default to False if missing
        'httpOnly': cookie.get('httpOnly', 'false').lower() == 'true',  # Convert to boolean & Default to False if missing
    }

# Only add cookies that match the current domain
if cookie_dict['domain'] in ['.amazon.com', 'www.amazon.com']:
    try:
        driver.add_cookie(cookie_dict) # Add cookie
    except Exception as e:
        print(f"Error adding cookie: {cookie_dict}, Error: {str(e)}")  # Print error message

sleep(5) # Wait for a bit before refreshing
driver.refresh()

# Print the current cookies
print(driver.get_cookies()) 

driver.close() # Close the browser
