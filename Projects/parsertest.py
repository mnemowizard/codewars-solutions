import requests
import json
from bs4 import BeautifulSoup

# url = 'https://calorizator.ru/product'
#
headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}
#
# req = requests.get(url, headers = headers)
# src = req.text
# print(src)

# with open('index.html', 'w', encoding = 'utf-8') as file:
#     file.write(src)

# with open('index.html' , encoding = 'utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_ = 'product')
# all_categories_dict = {}
#
# for product_list in all_products_hrefs:
#     links = product_list.find_all("a")
#     for link in links:
#         item_text = link.text
#         item_href = 'https://calorizator.ru/' + link.get("href")
#
#         all_categories_dict[item_text] = item_href

with open("all_categories_dict.json", encoding = 'utf-8') as file:
    all_categories = json.load(file)

count = 0
for category_name , category_href in all_categories.items():
    if count == 0:
        category_name = category_name.replace(' ', '_')
        print(category_name)
        req = requests.get(url = category_href, headers=headers)
        src = req.text

        with open(f'data/{count}_{category_name}.html', 'w', encoding = 'utf-8') as file:
            file.write(src)

        with open(f'data/{count}_{category_name}.html', encoding = 'utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        
        count += 1
