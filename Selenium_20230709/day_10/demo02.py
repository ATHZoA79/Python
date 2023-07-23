from bs4 import BeautifulSoup as bs
import requests as req

url = 'https://www.mobile01.com/'

# req.get 是回傳doc格式資料 需要用text轉換成字串
# 若要加上header只要在url後方加上headers屬性即可
with req.get(url) as web:
    soup = bs(web.text, "html.parser")
    
# print(data.prettify())

title = soup.find('header')
print(soup)