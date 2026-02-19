import json

data = {"name": "Kendrick", "age": 38}
with open("data.json", "w") as file:
    json.dump(data, file, indent = 4)