import json

num_of_companies = int(input("Enter total num of companies: "))

company_details = {}

for i in range(num_of_companies):
    name = input("Enter name of company: ")
    company_dict = {}
    company_dict["official_name"] = input("Enter official name of company: ")
    company_dict["num_of_employees"] = int(input("Enter number of employees: "))
    num_of_founders = int(input("Enter number of founders: "))

    names_of_founders = []
    for num_founders in range(num_of_founders):
        founder_name = input("Enter name of founder: ")
        names_of_founders.append(founder_name)
    company_dict["names_of_founders"] = names_of_founders
    
    print(name, company_dict)
    company_details[name] = company_dict
print(company_details[name])