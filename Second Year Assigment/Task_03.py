## OUTPUTTING OF VALUES SHOULD NOT HAVE BEEN DONE INSIDE THE CONVERGE FUNCTION.
## SCORE = 18 MARKS OUT OF 20 MARKS

def converge(User_Number):
    if User_Number == 1:
        return (int(User_Number))
    elif User_Number % 2 == 0:
        User_Number = User_Number / 2
        print(int(User_Number))
    elif User_Number % 2 == 1:
        User_Number = (User_Number * 3) + 1
        print(int(User_Number))
    return converge(int(User_Number))

while True:
    try:
        User_Number = int(input("Please provide a number for the game -> "))
        if isinstance(User_Number, (int)):
            break
        else:
            print("You cant use that its not a number.")
    except ValueError:
        print("You cant use that its not a number.")

converge(User_Number)


