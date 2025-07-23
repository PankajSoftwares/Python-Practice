'''
Loops
A loop means to repeat something in the exact same way.
Types of loops are :
1. For Loop
2. While Loop
3. While True
4. Nested Loop

'''

#1. For loop

'''
For Loop
For loop is a loop that repeats something in a given range.
The range has a starting point, ending point and a steplgar
+1 is added to the ending point while defining a range. |
e.g: range(0,6) - here this will print from 0 to 5 only, 0,1,2,3,4,5
'''
'''

#Ex. 1. 
a = 10
for i in range (0, 6):
    print(i) # output: from 0 to 5
    print(a) # output: 5 times 10

'''
'''

#Ex. 2
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end = " ")
    print()

'''
'''
Output for ex2. will be 

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''
#Ex.3 Table of n any number or 5
table_for= int(input("Enter the number for which you want table: "))
n = 10
for i in range(1,n+1):
    print(table_for,"x", i,"=", table_for * i)





### While Loop

