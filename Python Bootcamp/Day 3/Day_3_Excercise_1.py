number = int(input("Please provide a numbe to check: "))

odd_even_check = number % 2

if odd_even_check == 1:
    print("The number is Odd")
else:
    print("The number is even")