import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
print("Interface status")
print("=" * 50)
for x in data["imdata"]:
    att = x["l1PhysIf"]["attributes"]
    if att["id"] in ["eth1/33", "eth1/34", "eth1/35"]:
        print("DN:", att["dn"])
        print("Description:", att["descr"])
        print("Speed:", att["speed"])
        print("MTU:", att["mtu"])
        print("-" * 50)