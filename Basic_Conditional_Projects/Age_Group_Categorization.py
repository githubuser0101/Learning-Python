your_age = int(input("Enter your age: "))

if your_age < 0:
    print("The universe is waiting for you.")
elif your_age < 13:
    print("You are a child.")
elif your_age <20:
    print("You are a teenager.")
elif your_age < 60:
    print("You are an adult.")
elif your_age < 101:
    print("You are a senior citizen.")
else:    
    print("Death shall have you soon!")