import json

names = {"name": "Vik", "age": 21}

example = json.dumps(names)

print(type(example))

json_data = open("json_data.json", "w")

json_data.write(example)

json_data.close()