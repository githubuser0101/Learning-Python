marks = 66

if marks > 100 or marks < 0:
    print("Invalid marks entered")
    exit()

if marks > 89:
    print("Grade: A")
elif marks > 79:
    print("Grade: B")
elif marks > 69:
    print("Grade: C")
elif marks > 59:
    print("Grade: D")
else:
    print("Grade: F")

