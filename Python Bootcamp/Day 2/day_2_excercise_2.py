height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = (int(weight) / (float(height) ** 2))
bmi = int(bmi)

print("Your BMI score is " + str(bmi))