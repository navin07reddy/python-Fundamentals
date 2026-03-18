class ATM:
    def __init__(self, username, pin, balance):
        self.username = username
        self.pin= pin
        self.balance=balance

    def login(self):
        print("enter the user_name and pin")
        attempts=3
        while attempts > 0:
            user= input("enter the user name  ")
            pin= int(input("enter the pin"))
            if user == self.username and pin == self.pin :
                print("login sucess")
                return True
            else:
                attempts -=1
                print ("invalid details")
                print ("try again later")
                print("attempts left",{attempts})
                return False
    def deposit(self):
        amount =float(input("enter the amount"))
        self.balance += amount
        print ("deposited successfully")

    def withdraw(self):
        amount = float(input("enter the amount"))
        if amount > self.balance:
            print ("insufficient amount")
        else:
            self.balance -= amount
            print({amount})
            print("withdrawal") 

    def check_balance(self):
        print("balance", self.balance)


user1=ATM("navin", 2727, 1000)
if user1.login():
    while True:
        print("\n  menu ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice=int (input("enter the choice"))
        if choice == 1:
            user1.deposit()
        elif choice == 2:
            user1.withdraw() 
              
        elif choice == 3:
            user1.check_balance() 
        else:
            print("invalid choice")
            

