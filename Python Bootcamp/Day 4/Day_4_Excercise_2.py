import random

names_string = input("Give me everybody's names, seperated by a comma. ->")
names = names_string.split(", ")

total_people = len(names)

person_picked = random.randint(0, total_people - 1)

print(names[person_picked])

# Another solution is variable = random.choice(names)