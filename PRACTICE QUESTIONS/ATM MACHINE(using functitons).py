balance = 1000

def check_balance():
    print("Your balance is =", balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Money deposited successfully")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash")
    else:
        print("Insufficient balance")