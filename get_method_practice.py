c = {"Number1": "Six",
    "Number2": "Five",
    "Number3": "Four"}

a = input("Number?: ")
b = c.get(a)
print(b)

if b == None:
    print(f"is not equal")
else:
    print("is equal")
#------
# aa = c.keys()
# bb = c.values()
# cc = c.items()

# print(aa)
# print(bb)
# print(cc)
#-------
