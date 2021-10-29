from bs4 import BeautifulSoup
import requests, re

def printProductsInfo(products, prices):
    index = 1
    for (key,product) in enumerate(products):
        product_name = product.get_text().strip()
        raw_price = prices[key].get_text().strip()
        product_price = re.sub(r'^$\n', '', raw_price, flags=re.MULTILINE)
        print(f'{index}.\n{product_name} - {product_price} NOK \n ')
        index += 1

URL = 'https://www.elkjop.no/INTERSHOP/web/WFS/store-elkjop-Site/no_NO/-/NOK/ViewStandardCatalog-Browse?CategoryName=no-windows-pc&CategoryDomainName=store-elkjop-ProductCatalog&SearchParameter=%26%40QueryTerm%3D*%26ContextCategoryUUID%3DnZ.sGQWGjcwAAAFxtS4ZE6vF%26discontinued%3D0%26online%3D1&SortingAttribute=ProductListPrice-asc&select-sort-refine=ProductListPrice-asc'
HEADERS = { "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' }

page = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')
printProductsInfo(soup.find_all(class_ = "product-name"), soup.find_all(class_ = "product-price"))