
number = 10
factorial = 1

# for i in range(1, number + 1) :
#     factorial *= i

while(number):
    factorial *= number
    number -= 1

print(factorial)