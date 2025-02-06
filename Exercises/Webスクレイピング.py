import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.python.org/blogs/")

soup = BeautifulSoup(r.content,"html.parser")

a_tags = soup.find_all('a')

url_list = []

for a_tag in a_tags:
    href = a_tag.get("href")

print(soup.find("ul",class_="list-recent-posts menu" ).text)
