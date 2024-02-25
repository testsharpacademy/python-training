# mydic = {101:"x",102:"y",103:"z"}
# print(mydic)

# mydic = {
#     "Brand":"Audi",
#     "Model":"X10",
#     "Year":2023
# }
# Example 1
# print(mydic["Brand"])
# print(mydic["Model"])

# using get()
# x = mydic.get("Brand")
# print(x)

# Changing the values in dic
# mydic = {
#     "Brand":"Audi",
#     "Model":"X10",
#     "Year":2023
# }
# mydic["Year"] = 2024
# print(mydic)

# reading a dictionary
# print only keys from dict
# mydic = {
#     "Brand":"Audi",
#     "Model":"X10",
#     "Year":2023
# }
# # print keys from dict
# for i in mydic:
#     print(i)
# # print values from dict
# for i in mydic.values():
#     print(i)
# # print values from dict
# for i in mydic:
#     print(mydic[i])
# # print key & values from dict
# for key,value in mydic.items():
#     print(key,value)

# mydic = {
#     "Brand":"Audi",
#     "Model":"X10",
#     "Year":2023
# }
# if "Model" in mydic:
#     print("Model exists!!")
# else:
#     print("Model doesn't exists!!")
# count no of items present in dictionary
# print(len(mydic))
# Adding an item to dictionary
# mydic = {
#     "Brand":"Audi",
#     "Model":"X10",
#     "Year":2023
# }
# mydic["Color"] = "Black"
# print(mydic)

# remove item from dictionary
# mydic = {
#     "Brand":"Audi",
#     "Model":"X10",
#     "Year":2023
# }
# mydic.pop("Brand")
# print(mydic)
# del mydic["Year"]
# print(mydic)
# mydic.clear()
# del mydic
# print(mydic)

# Copying dict
mydic = {
    "Brand":"Audi",
    "Model":"X10",
    "Year":2023
}
# #mydic1 = mydic.copy()
# mydic1 = mydic
# print(mydic1)

se1 = {1,2,4,4}
# se1[0] = 5
se1(3)
print(se1)
