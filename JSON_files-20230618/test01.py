import requests as rq
import json
import re
# Custom Module
import ReadJSONfromURL as rjson

while True:
	user_input = input("Enter Src (quit if enter nothing):")
	user_input = str(user_input)

	if user_input == '':
		break

	if re.search(r'^http', user_input):
		rjson.readURL(user_input)