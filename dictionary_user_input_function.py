##--
all_list = []
product_info_rows = {}
product_key = {}

def product_info():
    
    #product_info_rows = {}
    product_info_rows["category"] = input("Enter categories: ")
    product_info_rows["product"] = input("Enter products: ")
    product_info_rows["brand"] = input("Enter brands: ")
    
    product_key[product_info_rows["category"]] = product_info_rows
    #print(product_key)
    #return product_info_rows
    return product_key
def product_data():

        for i in range(2):
            product_profile = product_info()
            all_list.append(product_profile)
        return all_list
        #print(i)        
b = product_data()
#print(product_key)
#print(b)
# a = product_info_rows
# #print(a)
# print(product_info())

#for output_key, output_values in brand_master_dict.items():
#         for a in output_values.:
#             for nested_key, nested_values in output_values():
# ##vehicle is keys and electronics is values. It'll store all they keys and values of "Automobile" and "Electronics"
#                 print (f"{output_key} -- {output_values} -- {a}")















    # for nested_key,nested_values in output_values():
    #     for a in nested_values:
    #         print(f"{output_key} -- {nested_key} -- {a}")

# for output_key, output_values in product_info_rows.items():
#     for nested_k in output_values:
#         for a in nested_k:
#             print(f"{output_key} -- {nested_k} -- {a}") 



##--

# for output_key, output_values in brand_master_dict.items():
#     #vehicle is keys and electronics is values. It'll store all they keys and values of "Automobile" and "Electronics"
    
#     for nested_key,nested_values in output_values.items():
#         for a in nested_values:
#             print(f"{output_key} -- {nested_key} -- {a}")

#---
# for a in all_list:
#     for k, v in a.items():
#         print(f"{k} -- {v}") 
        




##---
# def user_input():
#       name = input("Enter your name: ")
#      age = int(input("Enter your age: "))
#      nationality = input("Enter your nationality: ")
#      return name, age, nationality
#  user_profile = user_input()
#  print(user_profile)
##----