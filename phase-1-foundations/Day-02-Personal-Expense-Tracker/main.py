#personal Expense Tracker

#importing the datetime module to validate date input
import datetime 


# Sample expenses data to work with
expenses = [
    {
        "name": "Data Sim card",
        "category": "Utility",
        "amount": 5500,
        "date": "2026-05-01"
    },
    {
        "name": "Buiscuit",
        "category": "Food",
        "amount": 500,
        "date": "2026-05-02"
    },
    {
        "name": "Trip to Kano",
        "category": "Transport",
        "amount": 4500,
        "date": "2026-05-03"
    },
    {
        "name": "football match",
        "category": "Personal",
        "amount": 250,
        "date": "2026-05-04"
    },
    {
        "name": "Ice cream",
        "category": "Food",
        "amount": 1500,
        "date": "2026-05-05"
    },
    {
        "name": "Koko and Kosai",
        "category": "Food",
        "amount": 500,
        "date": "2026-05-06"
    },
    {
        "name": "Recharge card",
        "category": "Utility",
        "amount": 500,
        "date": "2026-05-07"
    },
    {
        "name": "Laptop stand",
        "category": "Utility",
        "amount": 3500,
        "date": "2026-05-08"
    },
    {
        "name": "Laptop battery",
        "category": "Utility",
        "amount": 30000,
        "date": "2026-05-09"
    },
    {
        "name": "Football match",
        "category": "Personal",
        "amount": 250,
        "date": "2026-05-10"
    }
]




# This program allows users to track their personal expenses by adding, viewing, summarizing, and deleting expenses. Each expense has a name, category, amount, and date. The program provides a menu for users to interact with their expenses and view summaries of their spending habits.
print("Welcome to your personal expense tracker!")
user_name = str(input("Please enter your name: "))
print(f"Hello, {user_name}!")

#the categories of expenses allowed in the program
categories = ("Food", "Transport", "Utility", "Business", "Personal")

#functions to add, view, summarize and delete expenses from the list of expenses
def add_expense(name, category, amount, date):
    new_expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }
    expenses.append(new_expense)
    print("Expense added successfully!")

def view_expenses():
    print("\nView all expenses:")
    for expense in expenses:
        print(f"{expense['date']}: {expense['name']} - {expense['category']} - N{expense['amount']}")


def get_summary():
    print("\nView summary:")
    if not expenses:
        print("No expenses recorded yet!.")
        return
    total_expenses = sum(expense["amount"] for expense in expenses)
    most_expensive = max(expenses, key=lambda x: x["amount"])
    total_by_category = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in total_by_category:
            total_by_category[category] += amount
        else:
            total_by_category[category] = amount
    cheapest = min(expenses, key=lambda x: x["amount"])
    print(f"Cheapest expense: {cheapest['name']} - N{cheapest['amount']}")
    print(f"Most expensive expense: {most_expensive['name']} - N{most_expensive['amount']}")
    print(f"\nTotal Expenses: N{total_expenses:.2f}")
    print("\nExpenses by Category:")
    for category, total in total_by_category.items():
        print(f"{category.capitalize()}: N  {total:.2f}")

def delete_expense(name_of_expense):
    for expense in expenses:
        if expense["name"].lower() == name_of_expense.lower():
            expenses.remove(expense)
            print("Expense deleted successfully!")
            break
    else:
        print("Expense not found.")


# Main loop to interact with the user and perform actions based on their choices
while True:
    print("\nPlease choose an option:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View summary")
    print("4. Delete an expense")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter the name of the expense: ")

        while True:
            
            category = input("Enter the category of the expense (Food, Transport, Utility, Business, Personal): ")
            if category.capitalize() in categories:
                break
            else:
                print("Invalid category. Please enter one of the following: Food, Transport, Utility, Business, Personal.")
             
        while True:
            try:        
                amount = float(input("Enter the amount of the expense: "))
                if amount <= 0:
                    print("Invalid input. Please enter a number greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue
        while True:
            date = input("Enter the date of the expense (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
                continue  

        add_expense(name, category.capitalize(), amount, date)

    elif choice == "2":
        view_expenses()
    elif choice == "3":
        get_summary()
    elif choice == "4":
        name_of_expense = input("Enter the name of the expense to delete: ")
        delete_expense(name_of_expense)
    elif choice == "5":
        print("Thank you for using the personal expense tracker! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")