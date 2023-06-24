# List = Used to store multiple iteams in a single variable

food = ["pizza", "hamburgers", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

food.append("ice cream") # Adds to list
food.remove("hotdog") # Removes
food.pop() # Removes last element
food.insert(0,"cake") # Adds to position
food.sort() # Sorts alphabetically
#food.clear() # Clears list

print(food[1])

for x in food:
    print(x)