# Password system with attempts
password = "admin123"
for i in range(3):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")

else:
    print("Account Locked")