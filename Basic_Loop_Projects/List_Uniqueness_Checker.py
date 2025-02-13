items = ["apple", "banana", "carrot", "apple"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item found: ", item)
        # print(unique_items)
        exit()
    else:
        unique_items.add(item)
print("No Duplicate item found.")