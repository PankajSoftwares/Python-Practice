'''
#1.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''
for i in range(1, 6): #rows
    for j in range(1, i+1): # Columns
        print(j, end = (" "))
    print()
'''
'''
#2.

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
code: 
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end = " ")
    print()
'''

'''
#3.
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
code: 
for i in range (1,6): #rows
    for j in range (6, i, -1): #columns
        print(i, end = " ")
    print()
    
'''
'''
#4.
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
code:
'''
'''
for i  in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
'''

'''
#5. 
So here we have to print the space also

        *
      * *
    * * *
  * * * *
* * * * *
'''
'''
for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end = " ")

    for k in range(i):
        print("*", end = " ")
    print()

'''
'''

# 6.
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5

'''
'''
for i in range(5, 0, -1):
    for j in range(1, i):
        print(" ", end = " ") #Space

    for k in range(i, 6):
        print(k, end = " ")
    print()
'''
'''
    explainations✅ i = 5:
range(1, 5) → 4 spaces

range(5, 6) → prints: 5
 
'''

'''
#7.

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

code:

'''
'''

for i in range(1,6):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()
'''

'''
#8.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

code: 
'''
'''
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end = " ")
    print()
for i in range(4, 0, -1):
    for k in range(i, 0, -1):
        print("*", end = " ")
    print()
'''

'''
#10. patter for multiplications like this
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36

code: 
'''

for i in range (1, 7):
    for j in range(1, i+1):
        print(i*j, end = " ")
    print()