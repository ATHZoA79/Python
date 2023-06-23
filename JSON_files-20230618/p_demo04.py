from urllib.request import urlopen   # 網路傳輸
import json

with urlopen("https://datacenter.taichung.gov.tw/swagger/OpenData/84bc5a49-63d4-4fb4-98c4-c01b24d42dbe") as file:
    data = json.loads(file.read())
    print(data)
