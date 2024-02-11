target = int(input()) # Enter a number between 0 and 1000

even_sum = 0

for number in range(2, target + 1, 2):
    even_sum += number

print(f"The total is {even_sum}")