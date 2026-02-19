import json

x =  '{ "name":"John", "age":30, "city":"New York"}' #json

y = json.loads(x) #converting to py

print(y)
print(y["age"])