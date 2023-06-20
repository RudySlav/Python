# Logical Operators (and, or, not)
# Used to check if two or more conditional statments

temp = int(input("What is the temparture outside?: "))

if not(temp >= 0 and temp <=30):
    print("The temparature is bad today!")
    print("Stay Inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")
