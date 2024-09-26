from helper import Automation, AmazonShopping


# item1 = Automation('Chrome', 'https://www.amazon.com', 'iPhone')
# item1.open_browser()
# item1.search_string()
# item1.close_browser()

item = '(Renewed) Apple iPhone 8, US Version, 64GB, Space Gray - Unlocked'
item1 = AmazonShopping('Chrome', 'https://www.amazon.com', 'iPhone', item)
item1.open_browser()
item1.search_string()
item1.click_product()
item1.add_to_cart()
item1.close_browser()
