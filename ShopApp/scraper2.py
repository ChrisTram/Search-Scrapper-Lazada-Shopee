import requests
from urllib.parse import urlencode

list_of_urls = ['https://www.lazada.vn/catalog/?q=son+li']
# for individual products
for url in list_of_urls: 
    params = {'api_key': 'a0bc68f74a763a1b622e6b3ba97567a0', 'url': url}
    response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
    print(response.text)