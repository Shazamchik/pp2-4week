import json

x = { #py 
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(json.dumps(x, sort_keys = True)) #converting to json
