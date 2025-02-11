transportation_mode = "" 
distance = 18

if distance < 3:
    transportation_mode = "Walk"
elif distance < 16:
    transportation_mode = "Bike"
else:
    transportation_mode = "Car"

print(transportation_mode)