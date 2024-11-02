from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()
driver.maximize_window()



url = "https://www.homedepot.com/p/Outdoor-Essentials-5-8-in-x-5-1-2-in-x-6-ft-Pressure-Treated-Pine-Dog-Ear-Fence-Picket-102560/202319053"
driver.get(url)
# response = requests.get(url)
html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')
script_element = soup.find('script', id='thd-helmet__script--productStructureData')
script_content = script_element.string

# print(script_content)
data = json.loads(script_content)
title = data.get("name")
images = data.get("image")
description = data.get("description")
product_id = data.get("productID")
sku = data.get("sku")
gtin13 = data.get("gtin13")
brand = data.get("brand").get("name")
price = data.get("offers").get("price")
currency = data.get("offers").get("priceCurrency")
availability = data.get("offers").get("availability")

print(title)
print(images)
print(description)
print(product_id)
print(sku)
print(gtin13)
print(brand)
print(price)
print(currency)
print(availability)