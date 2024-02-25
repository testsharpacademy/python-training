# example 1:
# myset = {"Apple","Banana","Cherry"}
# print(myset) # unordered

# example 2: Accessing the elements from set
# myset = {"Apple","Banana","Cherry"}
# for i in myset:
#     print(i)

# example 3: Checking item is present in set
# myset = {"Apple","Banana","Cherry"}
# print("Banana" in myset)
# print("Banana1" in myset)

#exampe 4: Adding an element using Add() & Update()
# myset = {"Apple","Banana","Cherry"}
# myset.add("Orange") # adding a single item
# print(myset)
#
# myset.update(["Kiwi","Melon"])
# print(myset)

# Example 5: Counting the number of items present in set
# myset = {"Apple","Banana","Cherry"}
# print(len(myset))

# Example 6: Removing an item from set - remove() & discard()
# myset = {"Apple","Banana","Cherry"}
# print(myset)
# # myset.remove("Banana")
# # print(myset)
# # myset.remove("XYZ") #It will return Key error
# myset.discard("XYZ") # it will not throw any error
# print(myset)
# Example 7: Clearing the items from set
# myset = {"Apple","Banana","Cherry"}
# myset.clear()
# print(myset)
# del myset
# print(myset)
# example 8: Joining the 2 sets
myset = {"Apple","Banana","Cherry"}
set1={1,2,3}
set2={"a","b","c"}
# set3 = set1.union(set2)
# print(set3)
set1.update(set2)
print(set1)







