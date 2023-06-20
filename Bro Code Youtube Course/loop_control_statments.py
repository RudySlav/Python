# Loop Control Statments = Change a loops execution from its normal sequence
# break = Used to terminate the loop entirely
# continue = Skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "056-254-8569"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)