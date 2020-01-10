country_codes = {"US": "+1",
                "IN" : "+91",
                "UK": "+44",
                "AUS": "+61",
                "IT": "+39",
                "SA": "+966"}
#only keys
print(country_codes, "\n")
#only values
print(country_codes.values(), "\n")
#you get keys and values
print(country_codes.items())

for country_abrv in country_codes.keys():
    print(country_abrv)
for country_code in country_codes.values():
    print(country_code)
for country_abrv, country_code in country_codes.items():
    print(country_abrv, "--", country_code)
print(country_codes["IN"])
country_codes["SIN"] = "+65"
print(country_codes)