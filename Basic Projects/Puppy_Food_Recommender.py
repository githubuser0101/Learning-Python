pet = "Dog"
age = 1
food = ""

if pet == "Cat":
    food = "Senior Cat Food" if age > 5 else "Junior Pet Food"
elif pet == "Dog":
    food = "Puppy Food" if age < 2 else "Big Dawg Food"

print(food)

