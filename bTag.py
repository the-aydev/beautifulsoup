import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefing-room/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    try:
        a_tag = h2_tag.find('a')
        urls.append(a_tag.attrs['href'])
    except:
        pass

print(urls)
print(soup.prettify())
print(soup.find('b'))
print(soup.find('p'))
