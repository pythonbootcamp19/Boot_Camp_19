#input_country_abr = input("Enter the country abr: ")

country_names = {"IN": "India",
                "US": "USA",
                "UK": "United Kingdom",
                "AUS": "Australia",
                "IT": "Italy",
                "SA": "Saudi Arabia",
                "SIN": "Singapore"}

country_codes = {"US": "+1",
                "IN" : "+91",
                "UK": "+44",
                "AUS": "+61",
                "IT": "+39",
                "SA": "+966"}

while True:
    input_country_abr = input("Enter the country abr: ")

    name = country_names.get(input_country_abr)
    code = country_codes.get(input_country_abr)

    if name == None:
        input_name = input("Enter full name of country:")
        input_code = input("Enter country code: ")
        country_codes[input_country_abr] = input_code
        country_names[input_country_abr] = input_name
        print(f"added {input_name} successfully")
    else:
        print(name, code)
#print(country_names[input_country], country_codes[input_country])
