from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
import quickstart


def get_data(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    sleep(3)
    # response = requests.get(url)
    html_content = driver.page_source

    soup = BeautifulSoup(html_content, 'html.parser')
    script_element = soup.find('script', id='thd-helmet__script--productStructureData')

    if script_element is not None:
        script_content = script_element.string
    # print(script_content)

    # print(script_content)
        data = json.loads(script_content)
        try:
            title = data.get("name")
            image_s = data.get("image")
            images = "; ".join(image_s)
            description = data.get("description")
            product_id = data.get("productID")
            sku = data.get("sku")
            gtin13 = data.get("gtin13")
            brand = data.get("brand").get("name")
            try:
                price_element = soup.find('div', class_='price-format__large price-format__main-price')
                price = price_element.get_text()
            except:
                try:
                    price_element = soup.find('div', class_='price-detailed__unit-price price-detailed__alt-price')
                    price = price_element.get_text()
                except:
                    price = data.get("offers").get("price")
                    
            try:
                currency = data.get("offers").get("priceCurrency")
                availability = data.get("offers").get("availability")
            except:
                currency = "USD"
                availability = "InStock"
                
                
        except:
            pass
        try:
            print("url: ")
            print(url)
            print("title: ")
            print(title)
            print("images: ")
            print(images)
            print("description: ")
            print(description)
            print("product_id: ")
            print(product_id)
            print("sku: ")
            print(sku)
            print("gtin13: ")
            print(gtin13)
            print("brand: ")
            print(brand)
            print("price: ")
            print(price)
            print("currency: ")
            print(currency)
            print("availability: ")
            print(availability)
        except:
            pass
        quickstart.main()
        columnCount = quickstart.getColumnCount()
        RANGE_NAME_INDEX = f'scraping!A{columnCount + 2}:A'
        RANGE_NAME_URL = f'scraping!B{columnCount + 2}:B'
        RANGE_NAME_TITLE = f'scraping!C{columnCount + 2}:C'
        RANGE_NAME_IMAGES = f'scraping!D{columnCount + 2}:D'
        RANGE_NAME_DESCRIPTION = f'scraping!E{columnCount + 2}:E'
        RANGE_NAME_PRODUCT_ID = f'scraping!F{columnCount + 2}:F'
        RANGE_NAME_SKU = f'scraping!G{columnCount + 2}:G'
        RANGE_NAME_GTIN13 = f'scraping!H{columnCount + 2}:H'
        RANGE_NAME_BRAND = f'scraping!I{columnCount + 2}:I'
        RANGE_NAME_PRICE = f'scraping!J{columnCount + 2}:J'
        RANGE_NAME_CURRENCY = f'scraping!K{columnCount + 2}:K'
        RANGE_NAME_AVAILABILITY = f'scraping!L{columnCount + 2}:L'
        RANGE_NAME_CURRENT_TIME = f'scraping!N{columnCount + 2}:N'

        quickstart.insert_data(RANGE_NAME_INDEX, RANGE_NAME_URL, RANGE_NAME_TITLE, RANGE_NAME_IMAGES, RANGE_NAME_DESCRIPTION, RANGE_NAME_PRODUCT_ID,
                               RANGE_NAME_SKU, RANGE_NAME_GTIN13, RANGE_NAME_BRAND, RANGE_NAME_PRICE, RANGE_NAME_CURRENCY, RANGE_NAME_AVAILABILITY, RANGE_NAME_CURRENT_TIME, 
                               columnCount, url, title, images, description, product_id, sku, gtin13, brand, price, currency, availability)