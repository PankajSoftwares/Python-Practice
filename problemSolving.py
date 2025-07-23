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

#7 To find Single digit no.s, double digit no. etc

num = int(input("Enter a number: "))
if num > 0 and num <= 9: print(num, " is Single digit!")
elif num >= 10 and num <=99: print(num," is Double Digit!")
elif num >= 100 and num <=999: print(num," is Triple Digit!")