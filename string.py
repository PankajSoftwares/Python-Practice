'''
Strings are the combination of number, symbols, letter, enclosed inside quotations.

Creation of a String: Strings can be created by enclosing numbers, letters, enclosed inside quotations.

a = "Hello World!"
'''

a = "Hello World!"
print(a)
print(type(a))
print(a.upper())
print(a.lower()) # Lower case
print(a.strip()) #
print(len(a)) #to find length
print(a.count("l")) #to count the letter
print(a.find("l"))
print(a.rfind("l"))
print(a.rfind("l", 0, -1))
print(a.find("l", 0, -1))
print(a.index("l", 0, -1))

print(a.capitalize()) # first Letter Capitalize for the first word

name = "Pankaj"
age = 26
b = "My name is {} and i'm {} years old"
print (b.format(name, age)) # to print {} letter here

print(name.center(50, "*"))  # Centralize the word i give

print(len(b)) # to find length of sentence

print(name.count("a"))  # count the char

print(name.lower())
print(name.upper())

print(name.capitalize()) # To convert First letter to Capital
print(name.find("aj")) # To show the index value of a letter

print(a.casefold()) # convert the sentence into small letter

print(name.index("k")) # To find the index of the letter

print(a, a.isalnum()) # To check alphnumeric or not?

alphanumeric = "123Hello"
print(alphanumeric, alphanumeric.isalnum())

digit = "12345"
print(digit, digit.isdigit())
print(len(digit))

print(digit, digit.isdecimal())

# endswith() - return true if the string end with the specified value

a = "Harry Potter"
print(a.endswith("r"))
print(a.endswith("t", 6,9))
print(a.endswith("potter"))
print(a.lower().endswith("potter"))

print(a.startswith("h"))

print(a.swapcase()) # to Swapping of the case from upper to lower and vice versa

a = "      ******* Harry Potter    ....."
print(a)
print(a.strip()) # it will remove extra things space
print(a.strip("*, ")) # it will remove extra things space like
# print("\n")
# # print( a.rstrip(".,") + a.lstrip(" *, "))

#To split
a = "OOFD#BRB#OMW#TB"
b = "hello. my name is pks and i 'm 23 years old"
print(a.split("#"))
print(a.split("O")) # it's spliting O (o)

# ljust : for left justifications

#print(" ")
c = "Hi There"
d = a.ljust(20, "*") #Left alignment
e = a.rjust(40,"&") #Right Alignment
print(d, "is my favorite song")
print(e, "is my favorite movie")

#replace: to replace the value in string

a = "My name is Richa"
print(a)
print(a.replace("Richa", "Pooja"))


# rindex: searched the string and returns the last index of a string.

a = "Hello, This is Bengaluru!"
print(a.rindex("Bengaluru")) # First letter index of any word or sentence

# rfind() : searches the string for a specified value and returns the last position where it found.

b = " hello, everyone my name is Pankaj Kumar Sharma"
print(b.rfind("K", 3, 90))

