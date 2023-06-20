import time
# For Loop = A statment that will execute it's block of code a limited amount
#            of times
#           While Loop = unlimited
#           For Loop = Limited

for i in range(10):
    print(i + 1)

for i in range(50,100 + 1,2):
    print(i)

for i in "Krzysztof Mendel":
    print(i)

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!")