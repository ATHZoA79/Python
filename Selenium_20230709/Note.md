# Web Scrapping
---
date: 2023-7-29
---
## Beautifulsoup
| Beautifulsoup是將取得到的網頁資料轉換成字串形式的套件，因此需要搭配其他網頁擷取套件
例如
* urllib.request
* requests
```
	url="https://www.ptt.cc/bbs/Gossiping/index.html"
	request = req.Request(url, headers={
		"Cookie":"over18=1",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
	})

	with req.urlopen(request) as response:
		data = response.read().decode("utf-8")
```
或
```
	import requests as req
	url = 'https://www.mobile01.com/'
	header = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
	}

	with req.get(url, headers=header) as web:
		soup = bs(web.text, "html.parser")
```
---
常用的DOM選擇方法如下，snake-case和camel-case是相同的功能(但是依照編寫標準應該用snake-case)
```
	soup.find("tag", class_="className")
	soup.find("tag", id="idName")
	find_all()	# 基本上只能用在class
	find_previous
	find_next
	find_parent
```

---
## Selenium 
| Selenium 是藉由程式自動操作網頁，所以只要做好設定就會自動開啟瀏覽器並如真實人物一樣進行網頁互動(滾動、點擊)
| 為了讓程式開啟瀏覽器，需要將對應瀏覽器的webdriver下載並移到專案資料夾(以下使用google webdriver)
設定及執行
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.chrome_executable_path="webdriver 的絕對路徑"
driver = webdriver.Chrome(options=options)

driver.get('http://127.0.0.1/anthony/demo01.html')

el_4 = driver.find_element(By.CLASS_NAME, "link-4")
el_4.click()

time.sleep(3)
```

---