# Nested Loops = The "inner loop" will finish all of it's interations before
#                finsihing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many collumns?: "))
symbol = input("Enter a sybmol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()