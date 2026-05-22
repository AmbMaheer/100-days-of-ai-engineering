import csv
import datetime 

# Load expenses ONCE at the start (Loads everyone's data in the background)
def load_expenses(filename="expenses.csv"):
    expenses = []
    try:
        with open(filename, "r", newline="") as rf:
            reader = csv.reader(rf)
            try:
                next(reader) 
            except StopIteration:
                return expenses 
                
            for row in reader:
            
                if not row or len(row) < 5:
                    continue
                    
                user, name, category, amount, date = row  
                expenses.append({
                    "user": user,            
                    "name": name,
                    "category": category,
                    "amount": float(amount),
                    "date": date
                })
    except FileNotFoundError:
        pass    
    return expenses

expenses = load_expenses()

print("Welcome to your personal expense tracker!")
# Get the active user's name and convert to lowercase for easy matching later on
active_user = input("Please enter your name: ").strip().lower()
print(f"Hello, {active_user.capitalize()}!")

categories = ("Food", "Transport", "Utility", "Business", "Personal")

def add_expense(user, name, category, amount, date):
    new_expense = {
        "user": user,                
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }
    expenses.append(new_expense)
    print("Expense added successfully!")

def view_expenses(current_user):
    print(f"\n{current_user.capitalize()}'s Expenses:")
    found = False
    for expense in expenses:
        # Only print if the name matches!
        if expense["user"] == current_user:
            print(f"{expense['date']}: {expense['name']} - {expense['category']} - N{expense['amount']}")
            found = True
            
    if not found:
        print("No expenses found for your account.")

def get_summary(current_user):
    print("\nView summary:")
    # Filter out only the current user's expenses into a temporary list
    user_expenses = [exp for exp in expenses if exp["user"] == current_user]
    
    if not user_expenses:
        print("No expenses recorded yet!")
        return
        
    total_expenses = sum(expense["amount"] for expense in user_expenses)
    most_expensive = max(user_expenses, key=lambda x: x["amount"])
    total_by_category = {}
    
    for expense in user_expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in total_by_category:
            total_by_category[category] += amount
        else:
            total_by_category[category] = amount
            
    cheapest = min(user_expenses, key=lambda x: x["amount"])
    
    print(f"Cheapest expense: {cheapest['name']} - N{cheapest['amount']}")
    print(f"Most expensive expense: {most_expensive['name']} - N{most_expensive['amount']}")
    print(f"\nTotal Expenses: N{total_expenses:.2f}")
    print("\nExpenses by Category:")
    for category, total in total_by_category.items():
        print(f"{category.capitalize()}: N{total:.2f}")

def delete_expense(current_user, name_of_expense):
    for expense in expenses:
        # Must match the expense name AND belong to the current user
        if expense["name"].lower() == name_of_expense.lower() and expense["user"] == current_user:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            break
    else:
        print("Expense not found in your account.")

def save_expenses(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="") as wf:
        writer = csv.writer(wf)
        
        writer.writerow(["user", "name", "category", "amount", "date"])
        for expense in expenses:
            writer.writerow([expense['user'], expense['name'], expense['category'], expense['amount'], expense['date']])


# Main loop 
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
        
        # Pass the active_user to the function
        add_expense(active_user, name, category.capitalize(), amount, date)
        save_expenses(expenses)

    elif choice == "2":
        # Pass the active_user so it only prints their data
        view_expenses(active_user)
    
    elif choice == "3":
        get_summary(active_user)
        
    elif choice == "4":
        name_of_expense = input("Enter the name of the expense to delete: ")
        delete_expense(active_user, name_of_expense)
        save_expenses(expenses)
        
    elif choice == "5":
        print(f"Thank you for using the personal expense tracker {active_user}! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")