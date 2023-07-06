row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x, y = int(position[0]), int(position[1])

if x == 1:
    row1[y - 1] = "X"
elif x == 2:
    row2[y - 1] = "X"
elif x == 3:
    row3[y - 1] = "X"
# another way is to do map[y - 1][x - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")