# Variable is a container Value

#String
first_name = "Krzysztof"
last_name = "Menz"
full_name = first_name +" "+ last_name
print(type(full_name))
print("Hello "+full_name)

#Integer
age = 23
age += 1
print("Your age is: "+str(age)) # Watch out for concatenation
print(type(age))

#Float
height = 250.5
print("Your height is: "+str(height)+"CM")
print(type(height))

#Boolean
human = False
print(human)
print("Are you a human: "+str(human))
print(type(human))

#Single Assgiment
name = "Kris"
age = 21
attractive = True

print(name)
print(age)
print(attractive)

#Multiple Assigment Example 1
name, age, attractive = "Bro", 21, True

#Multiple Assigment Example 2
Spongebob = Partick = Sandy = Squidward = 30

print(Spongebob)
print(Partick)
print(Sandy)
print(Squidward)