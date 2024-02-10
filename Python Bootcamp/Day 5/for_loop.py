# For Loop
# Do something to each iteam in a list
#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
#    print(fruit)
#    print(fruit + " Pie")

#For Loop Lesson 2
# Using for loop with range function
#for number in range (a,b):
#print number

for number in range(1, 11, 3): #steps by 1 by default, the 3 at the end is the step determinant
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)