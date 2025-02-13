n = int(input("Enter a number: "))
even_no_sum = 0
for i in range(2, n+1):
    even_no_sum += i if i % 2 == 0 else 0

print(even_no_sum)