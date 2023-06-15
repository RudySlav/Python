# Programming Project Total Score Achived = 83.05/100
# Krzysztof Mendel
KIDS_CLUB = 100
POOL_PASS = 150


def main():
    menu_loop()


#  Function to read in Data from Bookings File
def read_data(name_of_file):
    connection = open(name_of_file)
    type_of_accomodation = []
    cost_for_season = []
    amount_of_bookings = []
    for line in connection:
        line_data = line.split(',')
        type_of_accomodation.append(line_data[0])
        cost_for_season.append(int(line_data[1]))
        amount_of_bookings.append(int(line_data[2]))
    connection.close()
    return type_of_accomodation, cost_for_season, amount_of_bookings


# Function to append data back to the bookings file
def add_to_booking(t, c, a):
    with open("Bookings_2022.txt", "w") as f:
        for i in range(len(t)):
            print(f"{t[i]},{c[i]},{a[i]}", file=f)


# Function to read in Extra file into the program
def kids_pool_counter(name_of_file):
    connection = open(name_of_file)
    type = []
    amounts = []
    for line in connection:
        line_data = line.split(',')
        type.append(line_data[0])
        amounts.append(int(line_data[1]))
    connection.close()
    return type, amounts


# Function to append data back into the extras file
def add_to_kids_pool(b, t):
    with open("extras.txt", "w") as f:
        for i in range(len(b)):
            print(f"{b[i]},{t[i]}", file=f)


# Function to print out Menu and return users choice
def user_menu_choice():
    print("LONG ISLAND HOLIDAYS")
    print(20 * "=")
    print("1.Make a Booking")
    print("2.Review Bookings")
    print("3.Exit")
    num = -1
    while num < 0 or num > 3:
        try:
            num = int(input("Please select one of the above with the representing number only! ==> "))
        except ValueError:
            print("Please provide whole numbers only.")
    return num


# Function to loop the user into the new table
def menu_loop():
    choice = user_menu_choice()
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    while choice != 3:
        choice = user_menu_choice()


# Function that runs the booking choice when user selects it
def choice1():
    accomodation, cost, amount_booked = read_data("Bookings_2022.txt")
    type, amount = kids_pool_counter("extras.txt")
    total_bookings_made = amount_booked[0] + amount_booked[1] + amount_booked[2]
    price = 0
    pool_pass_cost = 0
    accomodation_type = ""
    pool_answear = ""
    booking_id = 1
    if total_bookings_made < 30:
        if total_bookings_made >= 1:
            booking_id = total_bookings_made + 1
        while True:
            surname = input("Enter Your Family Name => ")
            if len(surname) <= 0:
                print("You have not typed anything in.")
            elif len(surname) <= 14:
                break
            else:
                print("Your Surname is over the maximum characters allowed!")
        while True:
            phone_number = input("Enter Your Phone Number => ")
            if phone_number.isdigit():
                if len(phone_number) <= 0:
                    print("You have not typed anything in.")
                elif len(phone_number) <= 12:
                    break
                else:
                    print("Your phone number is over the allowed amount of characters!")
            else:
                print("Only digits are allowed")
        while True:
            accomodation_type_picked = int(input(
                f"Choose Your Accommodation type:\n1. Deluxe Caravan (€2000.0) {amount_booked[0]} booked\n2. Standard Caravan (1600.00) {amount_booked[1]} booked\n3. Camp Site (€200.0) {amount_booked[2]} booked\n4. No Booking\n==> "))
            if 0 >= accomodation_type_picked >= 5:
                print("That is not a correct choice")
            elif accomodation_type_picked == 4:
                break
            else:
                while True:
                    group_total = int(input("How many people in your group? ==> "))
                    if group_total <= 0:
                        print("Incorrect Amount of People")
                    else:
                        break
                while True:
                    pool_pass_query = input(
                        "Do you require a family pool pass? Please use Y or N as Your Answer ==> ").lower()
                    if pool_pass_query == "y" or pool_pass_query == "n":
                        if pool_pass_query == "y":
                            pool_answear = "Yes"
                        elif pool_pass_query == "n":
                            pool_answear = "No"
                        break
                    else:
                        print("That is not a correct choice.")
                while True:
                    kids_club_total = int(input("How many kids will join the kids club? ==> "))
                    if 1 <= kids_club_total < group_total:
                        break
                    else:
                        print("That's not correct")
                if accomodation_type_picked == 1:
                    price = 2000
                    amount_booked[0] += 1
                    accomodation_type = "Deluxe Caravan"
                elif accomodation_type_picked == 2:
                    price = 1600
                    amount_booked[1] += 1
                    accomodation_type = "Standard Caravan"
                elif accomodation_type_picked == 3:
                    price = 200
                    amount_booked[2] += 1
                    accomodation_type = "Camp Site"
                if pool_pass_query == "y":
                    pool_pass_cost = POOL_PASS
                    amount[1] += 1
                if kids_club_total > 0:
                    amount[0] += kids_club_total
                kids_club_cost = kids_club_total * KIDS_CLUB
                total_booking_price = price + pool_pass_cost + kids_club_cost
                print("Booking Details")
                print("-" * 20)
                print(f"Booking ID: {booking_id}")
                print(f"Accommodation Type: {accomodation_type}")
                print(f"Number of People: {group_total}")
                print(f"Pool Pass: {pool_answear}")
                print(f"Number for Kids Club: {kids_club_total}")
                print(f"Total Cost: {total_booking_price}")
                with open(f"{surname}{booking_id}.txt", "w") as connection:
                    print(f"{surname} {booking_id}", file=connection)
                    print("-" * 20, file=connection)
                    print(f"Booking ID: {booking_id}", file=connection)
                    print(f"Phone Number: {phone_number}", file=connection)
                    print(f"Accommodation Type: {accomodation_type}", file=connection)
                    print(f"Number of People: {group_total}", file=connection)
                    print(f"Pool Pass: {pool_answear}", file=connection)
                    print(f"Number for Kids Club: {kids_club_total}", file=connection)
                    print(f"Total Cost: {total_booking_price}", file=connection)
                connection.close()
                add_to_booking(accomodation, cost, amount_booked)
                add_to_kids_pool(type, amount)
        menu_loop()
    else:
        print("We are fully booked out!")
        menu_loop()

# Function to display the review page of bookings
def choice2():
    accomodation, cost, amount_booked = read_data("Bookings_2022.txt")
    type_of_extra, amount_of_extra = kids_pool_counter("extras.txt")
    total_bookings = (amount_booked[0] + amount_booked[1] + amount_booked[2])
    projected_income = ((2000 * amount_booked[0]) + (1600 * amount_booked[1]) + (200 * amount_booked[2]) + (
                KIDS_CLUB * amount_of_extra[0]) + (POOL_PASS * amount_of_extra[1]))
    average_income = projected_income / total_bookings
    sites_left = 30 - total_bookings
    num1 = amount_booked[0]
    num2 = amount_booked[1]
    num3 = amount_booked[2]
    print(f"There is {amount_booked[0]} booking made for the Deluxe Caravan.")
    print(f"There is {amount_booked[1]} booking made for the Standard Caravan.")
    print(f"There is {amount_booked[2]} booking made for the Camp Site.")
    print(f"There is {amount_of_extra[0]} of kids attending the kids club.")
    print(f"We have sold {amount_of_extra[1]} of pool passes.")
    print(f"Our projected income so far is {projected_income}€")
    print(f"The average income per booking(s) is {average_income}€")
    print(f"We have a total of {sites_left} sites left in our Resort.")

    if total_bookings >= 5:
        if (num1 > num2) and (num1 > num3):
            print("Our most popular type of accommodation is the Deluxe Caravan.")
        elif (num2 > num1) and (num2 > num3):
            print("Our most popular type of accommodation is the Standard Caravan.")
        elif (num3 > num2) and (num3 > num1):
            print("Our most popular type of accommodation is the Camp Site.")
    menu_loop()


if __name__ == '__main__':
    main()
