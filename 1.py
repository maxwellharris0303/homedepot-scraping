from bs4 import BeautifulSoup

html = '<div class="price-format__large price-format__main-price"><span class="price-format__large-currency-symbols">$</span><span>2</span><span hidden="">.</span><span class="price-format__large-currency-symbols">25</span></div>'

soup = BeautifulSoup(html, 'html.parser')
price_element = soup.find('div', class_='price-format__large price-format__main-price')
price = price_element.get_text()

print(price)