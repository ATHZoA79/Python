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

page_count = 0
label_count = 0
while page_count<5:
    titles = soup.find_all('div', class_="title")
    for title in titles:
        if title.a is not None:
            label_count += 1
            print( str(label_count) + title.a.text)
    prev_page_link = soup.find('div', class_="btn-group-paging").find('a', string='‹ 上頁')
    url = domain + str(prev_page_link['href'])
    request = req.Request(url, headers={
        "Cookie":"over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = bs(data, "html.parser")  
    page_count += 1
        
