print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your their? \n")

combined_names = name1 + name2

combined_names_lowercase = combined_names.lower()

t = combined_names_lowercase.count("t")
r = combined_names_lowercase.count("r")
u = combined_names_lowercase.count("u")
e = combined_names_lowercase.count("e")

true = t + r + u + e

l = combined_names_lowercase.count("l")
o = combined_names_lowercase.count("o")
v = combined_names_lowercase.count("v")
e = combined_names_lowercase.count("e")

love = l + o + v + e

answear = int(str(true) + str(love))


if answear < 10 or answear > 90:
    print(f"Your score is {answear}, you go together like coke and mentos")
elif answear > 40 or answear < 50:
    print(f"Your score is {answear}, you are alright together.")
else:
    (f"Your score is {answear}.")


