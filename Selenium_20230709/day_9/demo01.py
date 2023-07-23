import urllib.request as req
from bs4 import BeautifulSoup as bs

url="https://www.ptt.cc/bbs/Gossiping/index1.html"
request = req.Request(url, headers={
    "Cookie":"over18=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    
soup = bs(data, "html.parser")
titles = soup.find_all('div', class_="title")
for title in titles:
    # print(title)
    if title.a is not None:
        print(title.a)
        
    
# print(data)