
class BankAccount:
    def __init__(self, name):
        self.__balance = 0
        self.name = name
    
    def get_balance(self):
        print(f"BALANCE: ${self.__balance}")
    
    def deposit(self):

        amount = float(input("HOW MUCH ARE YOU DEPOSITING TODAY: "))

        if amount > 0 :
            self.__balance += amount
            print("DEPOSIT SUCCESSFUL")
        else:
            print("DEPOSIT UNSUCCESSFUL PLEASE TRY AGAIN")
    
    def withdrawal(self):
        amount = float(input("ENTER AMOUNT YOU WISH TO WITHDRAW: "))

        if amount <= 0:
            print("INVALID AMOUNT")
        elif amount > self.__balance:
            print("insufficient funds")
        
        else:
            self.__balance -= amount
            print("WITHDRAWAL SUCCESSFUL")

name = input("ENTER ACCOUNT HOLDER NAME: ")
account = BankAccount(name)
print(f"WELCOME MR {name}")
print("1.DEPOSIT")
print("2.WITHDRAW")
print("3.REQUEST BALANCE")
print("4.EXIT")
    
while True:
    option = input("ENTER YOUR CHOICE: ")
    if option == "1":
        account.deposit()
    elif option == "2":
        account.withdrawal()
    elif option == "3":
        account.get_balance()
    elif option == "4":
        print("thank you,bye bye")
        break
    else: 
        print("invalid option")



    

        


        






