'''
#1. positive or not

num = int(input("Enter a number: "))
if num > 0: print(num, "is Positive!")
else: print(num, "is not positive!")

'''
from tokenize import String

'''
#2. Even or odd number

num = int (input("Enter a number: "))
if num % 2 == 0: print(num, "is even")
else: print(num, "is odd number")

'''
'''
#3. Area of a square

side = int(input("Enter a side: "))
area = side * side
print("The area of square is:", area)

'''
'''
#4. Area of a triangle

base = int(input("Enter a base: "))
height = int(input("Enter a height: "))
area = (1/2) * base * height
print("The area of Triangle is:", area)
'''
'''
#5. Area of a Rectangle

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = width * length
print("The area of Rectangle is:", area)
'''
'''
#6 to find vowel letters

letter = input("Enter the letters: ")
if letter in "aeiou":
    print("The letter is a vowel letter")
else:
    print("The letter is not a vowel letter")


'''
'''
#7 To find Single digit no.s, double digit no. etc

num = int(input("Enter a number: "))
if num > 0 and num <= 9: print(num, " is Single digit!")
elif num >= 10 and num <=99: print(num," is Double Digit!")
elif num >= 100 and num <=999: print(num," is Triple Digit!")

'''
'''
#8 Problem Solving: From 1 to 50 sum of even numbers:
sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum += i

print(sum) // Output: 650

'''
'''
#9. prgm to write first 20 numbers and their sqaure

for i in range (1, 21):
    print(i, i*i)

'''
'''
#10. Print Pattern: row wise then i 
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
code: 

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
    
'''
'''
# 11. Print Pattern: Column wise then j
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
code:

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
'''

# 12. Print pattern like this
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

code:

for i in range (5,0,-1):
    for j in range (i, 0, -1):
        print(i, end=" ")
    print()

'''

'''
# 13. Print the pattern like this
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
code: 

for i in range (5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
'''
'''
# 14. Print the pattern like this

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
'''
for i in range(5, 0, -1):   #row
    for j in range(1, i+1): #column
        print(j, end=" ")   #Column
    print()                 #print to nextline
'''

#15. String Problem

a = "Hi, I am Python programming language!, not Java Programming language !"

print("The length of a is:",len(a))  # To find the length
b = (len(a))
print("The length of b is:",b)  #To print the length using using a verible

print("This is the count of o is: ",a.count("o")) # To a specific letter

print("1. This is the count of pro is:",a.count("Pro")) # To a specific word chars Case sensitive
print("2. Here we are counting All Pro:", a.count("Pro") + a.count("pro")) # To a specific word chars Case sensitive
print("3. Here we are counting all Pro incase sensitive: ", a.lower().count("pro"))

print("To change to lower case", a.lower()) # To Lower case
print("To change to UPPER CASE", a.upper())

z = a.title() # To Change to Title case
print(z)

print(a.find("Python")) # to find index number of Programming

print("")