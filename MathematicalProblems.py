'''
#2. Pelindrome

'''
num = int(input("Enter a number here: "))
temp = num
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

if rev == temp:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
