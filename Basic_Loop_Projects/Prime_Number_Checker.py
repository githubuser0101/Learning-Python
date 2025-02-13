import math
number = 11

for i in range(2, math.floor(number/2)):
    if number % i == 0:
        print("Not a prime no.")
        exit()
print("prime no.")