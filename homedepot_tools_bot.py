from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
from urllib.parse import urljoin
import getData
import getpass

pwd = getpass.getpass("Enter password: ")

if pwd == "run homedepot tools bot":
    pass
else:
    while(True):
        print("Incorrect password")
        sleep(10)

def scroll_down(driv):
    page_height = driv.execute_script("return document.body.scrollHeight")
    scroll_distance = page_height // 5
    driv.execute_script(f"window.scrollTo(0, {scroll_distance});")
    sleep(3)
    driv.execute_script(f"window.scrollTo({scroll_distance}, {scroll_distance * 2});")
    sleep(3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 2}, {scroll_distance * 3});")
    sleep(3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 3}, {scroll_distance * 4});")
    sleep(3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 4}, {page_height});")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.homedepot.com/b/Tools/N-5yc1vZc1xy")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "nav[class=\"customNav__container\"]")))

building_materials = driver.find_elements(By.CSS_SELECTOR, "nav[class=\"customNav__container\"]")[1]
building_materials_list = building_materials.find_elements(By.CSS_SELECTOR, "a[data-testid=\"anchor-link\"]")
building_materials_count = len(building_materials_list)
# print(building_materials_count)
new_urls = []
large_index = 0
while(large_index < building_materials_count):
    base_url = "https://www.homedepot.com/"
    list_url = building_materials_list[large_index].get_attribute('href')
    new_url = urljoin(base_url, list_url)
    new_urls.append(new_url) 
    large_index += 1
# print(new_urls)
medium_index = 0
while(medium_index < building_materials_count):
    driver.get(new_urls[medium_index])
    if medium_index == 0 or medium_index == 1 or medium_index == 2 or medium_index == 3 or medium_index == 4 or medium_index == 6 or medium_index == 7 or medium_index == 9 or medium_index == 10 or medium_index == 11 or medium_index == 12:
        sub_urls = []
        try:
            sub_list_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"sui-list-none sui-m-0 sui-relative sui-px-0 sui-py-2\"]")))
            sub_links = sub_list_element.find_elements(By.TAG_NAME, "a")
            for i in sub_links:
                sub_url = i.get_attribute('href')
                # print(sub_url)
                sub_urls.append(sub_url)
            # print(sub_urls)
            for url in sub_urls:
                driver.get(url)
                next_button_index = 0
                while(True):
                    try:
                        scroll_down(driver)
                        sleep(5)
                        products = driver.find_elements(By.CSS_SELECTOR, "div[class=\"browse-search__pod col__12-12 col__6-12--xs col__4-12--sm col__3-12--md col__3-12--lg\"]")
                    except:
                        try:
                            grid_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"results-layout__toggle results-layout__toggle-grid\"]")))
                            grid_button.click()
                            sleep(2)
                            scroll_down(driver)      
                            sleep(5)
                            products = driver.find_elements(By.CSS_SELECTOR, "div[class=\"browse-search__pod col__12-12 col__6-12--xs col__4-12--sm col__3-12--md col__3-12--lg\"]")
                        except:
                            pass

                    for product in products:
                        try:
                            product_link = product.find_element(By.TAG_NAME, "a").get_attribute('href')
                        except:
                            try:
                                product_link = product.find_element(By.CSS_SELECTOR, "a[class=\"product-image\"]").get_attribute('href')
                            except:
                                pass

                        getData.get_data(product_link)

                    try:
                        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[class=\"hd-pagination__item hd-pagination__button\"]")))
                        next_button = driver.find_elements(By.CSS_SELECTOR, "li[class=\"hd-pagination__item hd-pagination__button\"]")
                        print(next_button)
                        if next_button_index == 0:
                            next_url = next_button[0].find_element(By.TAG_NAME, "a").get_attribute('href')
                            driver.get(next_url)
                        else:
                            next_url = next_button[1].find_element(By.TAG_NAME, "a").get_attribute('href')
                            driver.get(next_url)
                    except:
                        try:
                            scroll_down()
                            WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[class=\"hd-pagination__item hd-pagination__button\"]")))
                            next_button = driver.find_elements(By.CSS_SELECTOR, "li[class=\"hd-pagination__item hd-pagination__button\"]")
                            print(next_button)
                            if next_button_index == 0:
                                next_url = next_button[0].find_element(By.TAG_NAME, "a").get_attribute('href')
                                driver.get(next_url)
                            else:
                                next_url = next_button[1].find_element(By.TAG_NAME, "a").get_attribute('href')
                                driver.get(next_url)
                        except:
                            break
                    next_button_index += 1       
        except:
            pass
    else:
        next_button_index = 0
        while(True):
            try:
                scroll_down(driver)
                sleep(5)
                products = driver.find_elements(By.CSS_SELECTOR, "div[class=\"browse-search__pod col__12-12 col__6-12--xs col__4-12--sm col__3-12--md col__3-12--lg\"]")
            except:
                try:
                    grid_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"results-layout__toggle results-layout__toggle-grid\"]")))
                    grid_button.click()
                    sleep(2)
                    scroll_down(driver)      
                    sleep(5)
                    products = driver.find_elements(By.CSS_SELECTOR, "div[class=\"browse-search__pod col__12-12 col__6-12--xs col__4-12--sm col__3-12--md col__3-12--lg\"]")
                except:
                    pass

            for product in products:
                try:
                    product_link = product.find_element(By.TAG_NAME, "a").get_attribute('href')
                except:
                    try:
                        product_link = product.find_element(By.CSS_SELECTOR, "a[class=\"product-image\"]").get_attribute('href')
                    except:
                        pass

                getData.get_data(product_link)

            try:
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[class=\"hd-pagination__item hd-pagination__button\"]")))
                next_button = driver.find_elements(By.CSS_SELECTOR, "li[class=\"hd-pagination__item hd-pagination__button\"]")
                print(next_button)
                if next_button_index == 0:
                    next_url = next_button[0].find_element(By.TAG_NAME, "a").get_attribute('href')
                    driver.get(next_url)
                else:
                    next_url = next_button[1].find_element(By.TAG_NAME, "a").get_attribute('href')
                    driver.get(next_url)
            except:
                break
            next_button_index += 1 
    medium_index += 1

driver.quit()