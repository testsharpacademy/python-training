# # Example 1: Creating the tuple
# mytuple = ("Apple","Banana","Cherry")
# print(mytuple)
# # example 2
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[-1])
# print(mytuple[-2])

# example 3 range of indexes
mytuple = ("Apple","Banana","Cherry","Melon","Mango","Kiwi")
# print(mytuple[2:5])
# print(mytuple[-4:-1])
#
# s = "Hellohhjhjhjh"
# print(s[1:4]) # ell
# print(s[2:4]) # ll
# print(s[-6:-3])
# print(mytuple[-6:-2:2])
# print(mytuple[2:6])
#example : 4
# mytuple = ("Apple","Banana","Cherry","Melon","Mango","Kiwi")
# By default tuple will not allow you to change the value because
# tuples are immutable
# tuple ---> list(tuple) --> modify --> tuple
# mytuple1 = ("apple","banana","cherry")
# mylist = list(mytuple1)
# mylist[0] = "orange"
# mytuple1 = tuple(mylist)
# print(mytuple1)
#
# for i in mytuple1:
#     print(i)

# Example 6: Check the item is present or not
#mytuple = ("Apple","Banana","Cherry","Melon","Mango","Kiwi")
#
# if "Apple" in mytuple:
#     print("Yes, Apple is present")
# else:
#     print("No, Apple is not present")

# Example 7: Count no of items present in tupple
mytuple = ("Apple","Banana","Cherry","Cherry","Mango","Kiwi")
# print(len(mytuple))
# print(mytuple.count("Cherry"))

# Example 8
# mytuple[0] = "Orange"
# print(mytuple)

# Example 9
# del mytuple
# print(mytuple)

# Example 10
# mytuple1 = (10,20,30)
# mytuple2 = ('a','b','c')
# mytuple3 = mytuple1 + mytuple2
# print(mytuple3)

# example 11 tupple comparision
# mytuple1 = (10,20,30)
# mytuple2 = (10,"Banana",30)
# if mytuple1==mytuple2:
#     print("tuples are equal")
# else:
#     print("tuples are not equal")
s1 = "hello"
s3 =" "
s2 = "world"
print(s1+s3+s2) #2254389956880 , 1750555283728











