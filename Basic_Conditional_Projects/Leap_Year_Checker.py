year = 2024

if (year % 4 == 0):
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Non-Leap Year")
    else:
        print("Leap Year")
else:
    print("Non-Leap Year")


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Non-Leap year")