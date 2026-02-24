import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
print("Interface status")
print("=" * 85)

for x in data["imdata"]:
    att = x["l1PhysIf"]["attributes"]
    if att["id"] in ["eth1/33", "eth1/34", "eth1/35"]:
        print(f"{att["dn"]:50} {att["descr"]:20} {att["speed"]:8} {att["mtu"]:6}")