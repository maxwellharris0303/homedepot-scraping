from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Define the proxy server
proxy_usage = False
proxy_server = 'http://144.172.123.97:3128'

# Create ChromeOptions object and set proxy settings
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy_server}')

# Create a new instance of the Chrome driver with the proxy options
while(True):
    driver = webdriver.Chrome() if not proxy_usage else webdriver.Chrome(options=chrome_options)

    # Make a request using the proxy
    driver.get('https://icanhazip.com/')
    proxy_usage = not proxy_usage

    # Print the page title
    print('Page Title:', driver.title)

    # Close the browser

    sleep(3)
    driver.quit()