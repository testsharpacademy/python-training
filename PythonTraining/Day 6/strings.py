import keyword

s="Welcome"
s='Welcome'
s = str("Welcome")
s = str('Welcome')

# create an empty string
name=""
name=''
name=str()

#Mutable : Change the value of the variable
#Immutable : cannot change the value of the variable

# s = 'hello'
# print(id(s))  #1792088750720
# s='python'
# print(id(s)) #1792086228016

# s="Welcome"
# print(s[0])
# s = "Qelcome"
# print(s[0])

# Example 3 Concatanation
# + , * with strings
# s="Welcome"
# print(s + "python") #
# print (s * 3) # WelcomeWelcomeWelcome
#print (s * 3 + "hi")
#slicing
# s = "Welcome"
# # starting index will start from 0
# # ending index will start from 1
# print(s[1:3]) # ec #el
#
# print(s[:6]) # Welcom
#
# print(s[2:]) # lcome
#
# print(s[1:-1]) # elcom
# print(s[1:-2]) #elco

# ord & chr
# print(ord('A'))
# print(chr(65))

# Max, Min & len
# s = 'abc'
# print(max(s)) #
# print(min(s)) #
# print(len(s)) #

# in & not in
# s = "welcome"
# print("come" not in s)


# String comparision
# print("tim" == "tie") # False
# print("free" != "freedom") #True
# print("arrow" > "aron") # True
# print("right" >= "left") # True
# print("teeth" < "tee") # False
# print("yellow" <= "fellow") # False
# print("abc" > "") # True

# s = "Welcome to python"
#
# print(s.isalnum())  #False
# print("Welcome".isalpha()) #True
# print("201d".isdigit()) #True
# print("2012".isalnum()) #True
# print("first Number".isidentifier()) #False
# print(s.islower()) # False
# print("WELCOME".isupper()) #True
# print(" ".isspace()) #True

# s = "Welcome to python"
# print(s.endswith("thon"))#True
# print(s.startswith("good")) #False
# print(s.find("come")) #3
# print(s.find("become")) #-1 not found
# print(s.count("o")) #3 returns no of occurences of substring in string

#
# # Converting string
# s = "String in PYTHON"
# s1=s.capitalize()
# print(s1) # String in python
#
# s2 = s.title()
# print(s2) # String In Python
#
# s3=s.lower()
# print(s3) # string in python
#
# s4=s.upper()
# print(s4) # STRING IN PYTHON
#
# s5 = s.swapcase()
# print(s5) #sTRING IN python"
#
# s6 = s.replace("in","on")
# print(s6) #String on PYTHON


# s = ["A","B","C","O","K","M"]
# #print(s[5:-2])
# s.remove("K")
# print(s)

s = "2323A"
print(s.isdigit())
#print(s.isalnum())










