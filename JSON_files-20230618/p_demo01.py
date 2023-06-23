import json 
jsonString = {
    "name": "John Doe"
}

anotherObject = '''
{
    "first": [ "andy", "bob", "claire", "daniel"]
}
'''

data = json.loads(anotherObject)
data["newKey"] = "new"

print(data)