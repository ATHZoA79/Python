import json 

with open("opendata_1.json", "r", encoding="utf8") as readFile:
	data = json.load(readFile)
	
print(data[0])