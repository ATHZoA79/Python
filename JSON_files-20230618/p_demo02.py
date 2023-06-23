import json 

with open("data.json") as jsonFile :
    data = json.load(jsonFile)

with open("data02.json", "r", encoding="utf-8") as data02:
    data2 = json.load(data02)

# print(data2.items()) 
print(data2)