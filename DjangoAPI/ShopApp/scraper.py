from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup



search ="son li"
client = ScraperAPIClient('a0bc68f74a763a1b622e6b3ba97567a0')

page = client.get(url='https://www.lazada.vn/catalog/?q=son+li&render=true', )

soup = BeautifulSoup(page.content, 'html.parser')
print(page.content)
results = soup.find_all(class_='RfADt')


print(results)

# col-xs-2-4 shopee-search-item-result__item