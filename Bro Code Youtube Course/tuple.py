# Tuple = Collection which is orderd and unchangeable used to group together
#         related data

student = ("Krzysztof", 22, "male")

print(student.count("Krzysztof")) # How many times specifed key appears
print(student.index("male")) # Index of specific value

for x in student:
    print(x)

if "Krzysztof" in student:
    print("Krzysztof is here")