balance = 0
transactions = []

def add_income(amount):
    global balance
    balance += amount
    transactions.append(("Income", amount))

def add_expense(amount):
    global balance
    balance -= amount
    transactions.append(("Expense", amount))

def show_balance():
    print("Current Balance: ", balance)


def show_transactions():
    print("\n--- Transactions ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for t_type, amount in transactions:
            print(f"{t_type}: {amount}₺")
    print("---------------------\n")



while True:
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Show transactions")
    print("5. Quit")

    choice = int(input("Choice: "))

    if choice == 1:
        income_balance = int(input("Enter income: "))
        add_income(income_balance)
        print("Current balance: ",balance)

    elif choice == 2:
        expense_balance = int(input("Enter expense: "))
        add_expense(expense_balance)
        print("Current balance: ", balance)

    elif choice == 3:
        show_balance()

    elif choice == 4:
        show_transactions()

    elif choice == 5:
        break