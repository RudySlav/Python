print("Welcome to the rollercoster!")

height = int(input("What is your height in cm? : "))

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5€")
    elif age <= 18:
        print("Please pay 7€")
    else:
        print("Please pay 12€")
else:
    print("Sorry, you are too short to ride the rollercoster.")

# > - Greater Than
# < - Less Than
# >= - Gratert than or equal to
# <= - Less than or equal to
# == - Equal To
# != - Not Equal to

