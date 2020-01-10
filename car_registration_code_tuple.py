registration_state = {"AP-02": "Andhra Pradesh",
                        "GJ-1": "Gujarat",
                        "HP-03": "Himachal Pradesh",
                        "HR-70": "Haryana",
                        "KA-01": "Karnataka",
                        "MH-01": "Maharashtra"}
                
registration_cities = {"AP-02": "Anantapur",
                        "GJ-1": "Ahmedabad",
                        "HP-03": "Shimla",
                        "HR-70": "Chandigarh",
                        "KA-01": "Bengaluru",
                        "MH-01": "Mumbai"}

while True:
        car_registration_code = input("Enter car registration code: ")

        state = registration_state.get(car_registration_code) 
        city = registration_cities.get(car_registration_code)

        if state == None:
            new_reg_code = input("Add car registration code: ")
            new_state_name = input("Add state: ")
            new_city_name = input("Add city name: ")

            registration_state[car_registration_code] = new_state_name
            registration_cities[car_registration_code] = new_city_name

            print(f"Car registration code {car_registration_code} added successfully")
        else:
            print (city,",", state)