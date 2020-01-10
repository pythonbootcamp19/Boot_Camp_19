list_of_cars = ["BMW", "Lexus", "Mercedez", "Tesla", "Tata", "Porche"]
list_of_bikes = ["Ducati", "Suzuki", "Honda", "Hero", "KTM", "Kawasaki"]
# print(list_of_cars)
# print(list_of_bikes)

automobile_brands = {"car": list_of_cars,
                    "bike": list_of_bikes}

# print("\n")
# #print(automobile_brands)

# print("\n")

# print(automobile_brands["bike"])
brand_list = automobile_brands["bike"]
#print(brand_list[0])

list_of_trucks = ["Tata", "Ashok", "Mahindra", "Eicher", "Volvo"]

automobile_brands["truck"] = list_of_trucks

for type_of_vehicle, list_of_brands in automobile_brands.items():
     #print(list_of_brands, "--", vehicles)
    for brand in list_of_brands:
        print(f"{type_of_vehicle} -- {brand}")
print("\n")    
# print(automobile_brands)

electronic_brands = {}
electronic_brands["phone"] = ["Apple", "Samsung", "MI", "Oneplus", "Huwai"]
electronic_brands["laptop"] = ["Apple", "Dell", "MSI", "Lenovo", "HP"]

print(electronic_brands)
print("\n")

brand_master_dict = {"Automobile": automobile_brands,
                    "Electronics": electronic_brands}
  
for output_key, output_values in brand_master_dict.items():
    #vehicle is keys and electronics is values. It'll store all they keys and values of "Automobile" and "Electronics"
    
    for nested_key,nested_values in output_values.items():
        for a in nested_values:
            print(f"{output_key} -- {nested_key} -- {a}")