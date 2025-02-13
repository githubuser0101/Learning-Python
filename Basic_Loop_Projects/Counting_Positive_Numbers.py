integers = [1, 2, 0, -1, -3, 5, 3, 7, 8, -9, 0]
positive_integer_count = 0
for i in integers:
    positive_integer_count += 1 if i > 0 else 0

print(positive_integer_count)