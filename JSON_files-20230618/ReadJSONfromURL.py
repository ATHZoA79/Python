import requests as rq
import json

def readURL(url):
	with rq.get(url) as req:
		data = req.json()
		print(json.dumps(data, indent=2, ensure_ascii=False))
		
def readFile(file):
	with rq.get(file) as req:
		data = req.json()
		print(json.dumps(data, indent=2, ensure_ascii=False))