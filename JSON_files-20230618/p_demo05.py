from urllib.request import urlopen   # 網路傳輸
import json

def scapper(url) :
    with urlopen(url) as file:
        data = file.read().decode("utf-8", "ignore")
        # json_data = json.loads(data.encode("utf-8"))
        print(json.dumps(data, indent=2))

while True :
    userInput = input("輸入路徑(輸入q結束)：")
    userInput = str(userInput)
    if userInput == 'q':
        break 
    scapper(str(userInput))