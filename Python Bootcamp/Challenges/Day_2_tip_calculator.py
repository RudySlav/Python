print("Tip Calculator")
amount = input("What is the total of the bill? -> ")
people = input("How many people are you spliting the bill with? -> ")
tip_amount = input("What % is the tip going to be 10% , 12% or 15%? -> ")

total_tip = int(amount) * (int(tip_amount) / 100) 

total_due = (int(amount) + total_tip) / int(people)
total_due = "{:.2f}".format(total_due)

print(f"The total due by each person is: {total_due}")