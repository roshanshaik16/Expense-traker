expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")

def show_expenses():
    if len(expenses) == 0:
        print("No expenses available.")
    else:
        print("\nYour Expenses:")

        for expense in expenses:
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("------------------------")

def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expenses:", total)

def save_expenses():
    file = open("expenses.txt", "w")

    for expense in expenses:
        file.write(
            str(expense["amount"]) + "," +
            expense["category"] + "," +
            expense["description"] + "\n"
        )

    file.close()
    print("Expenses saved successfully!")

def load_expenses():
    try:
        file = open("expenses.txt", "r")

        for line in file:
            amount, category, description = line.strip().split(",", 2)

            expense = {
                "amount": float(amount),
                "category": category,
                "description": description
            }

            expenses.append(expense)

        file.close()

    except FileNotFoundError:
        print("Starting with an empty expense list.")

# Main program

load_expenses()

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Save Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        save_expenses()

    elif choice == "5":
        save_expenses()
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
        