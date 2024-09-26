try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox import options
    from selenium.webdriver.firefox.options import Options
    from time import sleep


    class Automation:
        def __init__(self, browser, url, search):
            self.browser = browser
            self.url = url
            self.search = search

            if self.browser == "Chrome":
                self.driver = webdriver.Chrome(r'C:\chromedriver.exe')
            elif self.browser == "Firefox":
                option = Options()
                option.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
                self.driver = webdriver.Firefox(options=option, executable_path=r'C:\geckodriver.exe')
            else:
                print('Browser not found')

        def open_browser(self): 
            if self.browser == "Chrome":
                self.driver.get(self.url)
            elif self.browser == "Firefox":
                self.driver.get(self.url)
            else:
                print('Browser not found')

        def search_string(self):
            if 'geeksforgeeks' in self.url:
            
                self.driver.find_element(By.CSS_SELECTOR, '.gfg-icon_search').click()
                search_field = self.driver.find_element(By.ID, 'gcse-search-input')
                search_field.send_keys(self.search)
                search_field.send_keys(Keys.RETURN)
                sleep(5)
            elif 'amazon' in self.url:
                search_field = self.driver.find_element(By.ID, 'twotabsearchtextbox')
                search_field.send_keys(self.search)
                search_field.send_keys(Keys.RETURN)
                sleep(5)
            else:
                print('Search string not found')

        def close_browser(self):
            if self.browser == 'Chrome':
                self.driver.close()
            elif self.browser == 'Firefox':
                self.driver.close()
            else:
                print('Browser not found')


    class AmazonShopping(Automation):
        def __init__(self, browser, url, search, item_to_add):
            super().__init__(browser, url, search)
            self.item_to_add = item_to_add

        def open_browser(self):
            super().open_browser()
            self.product_name = ""
            self.rent = ""
            self.products = ""
            self.items = []
    
        def click_product(self):
            self.products = self.driver.find_elements(By.CLASS_NAME, 's-image')
            for prod in self.products:
                self.items.append(prod.get_attribute('alt'))
        
            for item in self.items:
                self.driver.implicitly_wait(10)
                if self.item_to_add in item:
                    self.driver.find_element(By.LINK_TEXT, item).click()
                    sleep(10)
                else:
           
                    pass

        def add_to_cart(self):
            self.driver.find_element(By.CSS_SELECTOR, '#submit\\.add-to-cart').click()
            sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

# website = Automation('Firefox', 'https://www.facebook.com', 'apple')

# website.open_browser()

# print(website.browser)
# print(website.search)
# print(website.url)