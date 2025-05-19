import re

from bs4 import BeautifulSoup

with open('index.html', encoding='utf-8') as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, 'lxml')

# page_h1 = soup.find('h1')
# print(page_h1)
#
# page_h1_all = soup.find_all('h1')
# print(page_h1_all)
#
# for items in page_h1_all:
#     print(items.text)

# user_name = soup.find('div', class_ = 'user__name')
# print(user_name.text.strip())

# user_name = soup.find('div', class_ = 'user__name').find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id" : "aaa"}).find("span").text
# print(user_name)

# find_all_span = soup.find(class_ = "user__info").find_all("span")
# print(find_all_span)

# for item in find_all_span:
#     print(item.text)


# print(find_all_span[0])
# print(find_all_span[2].text)

# link_to_social = soup.find(class_ = "social__networks").find_all("a")
# print(link_to_social)

# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")


# post_div = soup.find(class_ = "post__text").find_parent()
# print(post_div)
#
# post_divs =soup.find(class_ = "post__text").find_parents("div", "user__post__info")
# print(post_divs)

# next_el = soup.find(class_ = "post__title").next_element.next_element
# print(next_el)
#
# next_el = soup.find(class_ = "post__title").find_next().text
# print(next_el)

# next_sib = soup.find(class_ = "post__title").find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_ = "post__text").find_previous_sibling()
# print(prev_sib)

# links = soup.find(class_ = "some__links").find_all("a")
# print(links)
#
# for link in links:
#     link_text = link.text
#     link_data_attr = link.get("data-attr")
#     link_link = link.get("href")
#     print(f"{link_text}: {link_link} , {link_data_attr}")

finda_a_by_text = soup.find("a", text = re.compile("dl9"))
print(finda_a_by_text)