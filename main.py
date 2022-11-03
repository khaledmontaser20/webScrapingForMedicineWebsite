import requests
from bs4 import BeautifulSoup


result = requests.get("https://dwaprices.com/")
src = result.content

soup = BeautifulSoup(src, "html.parser")

cats = []
links=[]



category = soup.find_all("div", {"class":"innerUsesitem"})
print(category)
#
for i in range(len(category)):
    cats.append(category[i].text)
    links.append(cats[i].find_all("a").attrs['href'])
print(links)

