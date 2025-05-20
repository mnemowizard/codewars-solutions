import requests
from bs4 import BeautifulSoup

url = 'https://calorizator.ru/product'

headers = {
    'Accept': '*/*',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.3'
}

req = requests.get(url, headers = headers)
src = req.text
# print(src)

with open('index.html', 'w', encoding = 'utf-8') as file:
    file.write(src)