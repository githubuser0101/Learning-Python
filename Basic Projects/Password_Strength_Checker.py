password = "sljdlksd"
passwordLength = len(password)

if (passwordLength < 6):
    print("Weak")
elif (passwordLength < 11):
    print("Medium")
else:
    print("Strong")