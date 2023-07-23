from bs4 import BeautifulSoup as bs
import requests as req

url = 'https://www.mobile01.com/'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
}

# req.get 是回傳doc格式資料 需要用text轉換成字串
# 若要加上header只要在url後方加上headers屬性即可
with req.get(url, headers=header) as web:
    soup = bs(web.text, "html.parser")

header = soup.find('header')
head = soup.find('head')
print(head.prettify())