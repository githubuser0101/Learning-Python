while True:
    number = int(input("Enter a number between 1 and 10: "))
    # if number >= 1 and number <= 10:
    if 1 <= number <= 10:
        print("Correct Input!")
        break;
    else:
        print("Enter a valid number!")