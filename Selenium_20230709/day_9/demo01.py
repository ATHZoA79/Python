import urllib.request as req
from bs4 import BeautifulSoup as bs

url="https://www.ptt.cc/bbs/Gossiping/index.html"
request = req.Request(url, headers={
    "Cookie":"over18=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

domain = "https://www.ptt.cc"
soup = bs(data, "html.parser")  
prev_page_link = soup.find('div', class_="btn-group-paging").find('a', string='‹ 上頁')
next_page_link = soup.find('div', class_="btn-group-paging").find('a', string='下頁 ›')
print(prev_page_link['href'], next_page_link)
print("===============================")
