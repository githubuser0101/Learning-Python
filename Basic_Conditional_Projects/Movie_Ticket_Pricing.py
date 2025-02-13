def solution1():
    day = input("What day of the week is it: ")
    age = int(input("Enter your age: "))

    adult_ticket_price = 12
    child_ticket_price = 8
    price = "Your ticket price is {}" 

    if day == "Wednesday":
        if age >= 18:
            print(price.format(adult_ticket_price - 2))
            # print("Your ticket price is: $", adult_ticket_price - 2)
        else:
            print(price.format(child_ticket_price - 2))
            # print("Your ticket price is: $", child_ticket_price - 2)
    else:
        if age >= 18:
            print(price.format(adult_ticket_price))
            # print("Your ticket price is: $", adult_ticket_price)
        else:
            print(price.format(child_ticket_price))
            # print("Your ticket price is: ${child_ticket_price}")

# solution1()

def solution2():
    day = "Wednesday"
    age = 10 

    price = 12 if age >= 18 else 8 # ! A syntax of beauty
    if day == "Wednesday":
        price -= 2
    print(price)

solution2()