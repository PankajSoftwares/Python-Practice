'''
Continue: Skips a particular condition

Break: Stop or break the loop at a certain condition and comes out of the loop.
'''

''''
# 1. Continue: Skips the particular condition satisfying element

for i in range(1,11):
    if (i == 5):
        continue
    else:
        print(i)
'''

# 2. Breaks: the loop on condition Satisfy and comes out of the loop

for i in range(1, 11):
    if (i == 5): #Excluded the satisfying condition
        break
    else:
        print(i)

