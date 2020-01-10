state_names = {"KA": "Karnataka",
        "RJ" : "Rajasthan",
        "HR" : "Haryana",
        "PB" : "Punjab",
        "MH" : "Maharashtra",
        "AP" : "Andhra Pradesh"}

capital_names = {"Karnataka": "Bangalore",
                    "Rajasthan" : "Jaipur",
                    "Haryana": "Chandigarh",
                    "Punjab" : "Chandigarh",
                    "Maharashtra" : "Mumbai",
                    "Andhra Pradesh" : "Amravathi"}

population = {"Bangalore": "84.3 lakhs",
            "Jaipur": "30.7 Lakhs",
            "Chandigarh": "10.6 Lakhs",
            "Chandigarh": "10.6 Lakhs",
            "Mumbai":"1.84 Crores",
            "Amravati": "6.47 lakhs"}

for available_state_abr, available_state_names in state_names.items():
    print(available_state_abr, "--", available_state_names)

#input_state_abr = "KA"
input_state_abr = input("Enter state abr: ")
current_state = state_names.get(input_state_abr)
#current_populatin = population.get

if current_state == None:
    print(f"{input_state_abr} State not found")
else:
    print(current_state)
    current_capital = capital_names[current_state]
    current_population = population.get(current_capital)
    print(current_capital)
    print(current_population)