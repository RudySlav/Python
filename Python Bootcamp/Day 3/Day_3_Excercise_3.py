year = int(input("What year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not Leap year")