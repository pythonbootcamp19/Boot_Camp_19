import json

json_file = open("json_data.json")
json_dat_from_file = json_file.read()
print(json_dat_from_file)
#print(data_dict["age"])
data_dict = json.loads(json_dat_from_file)
# print(data_dict)
print(data_dict["age"])