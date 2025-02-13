import time

password = "abcdefgh"
wait_time = 1
attempts = 0
max_retries = 5

while max_retries:
    print("attempt: ", attempts + 1, "of 5")
    enteredPassword = input("Enter password: ")
    if (enteredPassword == password): 
        print("Correct Credential!")
        exit()
    else:    
        print("Password incorrect! Try again after", wait_time, "seconds")
        if attempts != 4: 
            time.sleep(wait_time)
        wait_time *= 2
        attempts += 1
        max_retries -= 1