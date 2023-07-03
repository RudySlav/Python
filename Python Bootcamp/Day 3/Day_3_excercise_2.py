height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = (int(weight) / (float(height) ** 2))
bmi = int(bmi)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, You are Underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, You are Normal Weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, You are Overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, You are Obese")
else:
    print(f"Your BMI is {bmi}, You are clinicaly Obese")