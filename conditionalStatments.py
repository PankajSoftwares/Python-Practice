'''
Allows Computer to execute a certain condition only if it is true.

Types of conditional statements
1. If
2. if...else
3. if .. elseif

'''
'''
#1. if

marks = int(input("Enter your marks: "))

if marks > 90:
    print("You will get a phone.")
print("Thank you!")


#2. if...else

run = int(input("Enter india's run: "))
target = int(input("Enter The current match target: "))

if run >= target:
    print("Well done, India won the match")
else:
    print("Sorry india, Opponent won the match")

'''

#3. if .. elif..

marks = int(input("Enter your marks (out of 100): "))

if marks >= 85:
    print("You passed with Distinction! 🎉")

elif marks >= 60:
    print("You passed with 1st Division!")

elif marks >= 45:
    print("You passed with 2nd Division!")

elif marks >= 33:
    print("You passed with 3rd Division!")

elif marks >= 0:
    print("You are Failed 😞")

else:
    print("Invalid marks entered.")
