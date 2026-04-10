correct_username = "elkan"
correct_password = "the great"
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts += 5

if attempts == 15:
    print("Account Locked")