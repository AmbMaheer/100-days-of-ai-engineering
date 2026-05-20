import datetime

expenses = [
    {"name": "Rent", "category": "Utility", "amount": 45000, "date": "2026-03-01"},
    {"name": "Groceries", "category": "Food", "amount": 12000, "date": "2026-03-05"},
    {"name": "Transport", "category": "Transport", "amount": 8000, "date": "2026-03-10"},
    {"name": "Data sim card", "category": "Utility", "amount": 5500, "date": "2026-03-15"},
    {"name": "Lunch", "category": "Food", "amount": 3500, "date": "2026-03-20"},
    {"name": "Rent", "category": "Utility", "amount": 45000, "date": "2026-04-01"},
    {"name": "Groceries", "category": "Food", "amount": 14000, "date": "2026-04-05"},
    {"name": "Transport", "category": "Transport", "amount": 9500, "date": "2026-04-10"},
    {"name": "Data sim card", "category": "Utility", "amount": 5500, "date": "2026-04-15"},
    {"name": "Lunch", "category": "Food", "amount": 3000, "date": "2026-04-20"},
    {"name": "Football match", "category": "Personal", "amount": 2000, "date": "2026-04-20"},
    {"name": "Rent", "category": "Utility", "amount": 45000, "date": "2026-05-01"},
    {"name": "Groceries", "category": "Food", "amount": 11000, "date": "2026-05-05"},
    {"name": "Transport", "category": "Transport", "amount": 7500, "date": "2026-05-10"},
    {"name": "Data sim card", "category": "Utility", "amount": 5500, "date": "2026-05-15"},
    {"name": "Lunch", "category": "Food", "amount": 4000, "date": "2026-05-18"},
]

print("Welcome to the Spending Forecaster!")
name = input("enter your name: ")
print(f"Hello, {name}!")


def calculate_monthly_average(expenses):
    monthly_totals = {}
    for expense in expenses:
        month = expense["date"][:7]
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += expense["amount"]
    
    overall_average = sum(monthly_totals.values()) / len(monthly_totals)
    return monthly_totals, overall_average


def analyze_category_trends(expenses):
    
    sorted_expenses = sorted(expenses, key=lambda x: x["date"])
    
    
    category_lists = {}
    for expense in sorted_expenses:
        category = expense["category"]
        if category not in category_lists:
            category_lists[category] = []
        category_lists[category].append(expense["amount"])

    trends = {}
    for category, amounts in category_lists.items():
        if len(amounts) < 2:
            trends[category] = "Not enough data"
            continue

        mid = len(amounts) // 2
        
        first_half = amounts[:mid]
        second_half = amounts[mid:]
        
        first_total = sum(first_half)
        second_total = sum(second_half)
        
        if second_total > first_total:
            trends[category] = "Up 📈"
        elif second_total < first_total:
            trends[category] = "Down 📉"
        else:
            trends[category] = "Flat ➖"            
    return trends

def forecast_next_30_days(expenses):
    dates = [datetime.datetime.strptime(expense["date"], "%Y-%m-%d") for expense in expenses]
    days_tracked = (max(dates) - min(dates)).days + 1
    total_expenses = sum(expense["amount"] for expense in expenses)
    daily_average = total_expenses / days_tracked
    forecast_total = daily_average * 30
    total_by_category = {}
    for expense in expenses:
        category = expense["category"]
        if category not in total_by_category:
            total_by_category[category] = 0
        total_by_category[category] += expense["amount"]
    category_forecast = {category: (total / days_tracked) * 30 for category, total in total_by_category.items()}
    return forecast_total, category_forecast

def calculate_saving_potential(expenses, income):
    monthly_totals, average_monthly_expense = calculate_monthly_average(expenses)
    
    savings = income - average_monthly_expense
    
    savings_percentage = (savings / income) * 100
    
    if savings_percentage >= 20:
        print("Verdict: Good")
    elif savings_percentage >= 10:
        print("Verdict: Tight")
    else:
        print("Verdict: Critical")
        
    return savings

while True:
    print("\nSpending Forecaster Menu:")
    print("1. Calculate Monthly Average")
    print("2. Analyze Category Trends")
    print("3. Forecast Next 30 Days")
    print("4. Calculate Saving Potential")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        monthly_totals, overall_average = calculate_monthly_average(expenses)
        print("\nMonthly Average Expenses:")
        for month, total in monthly_totals.items():
            print(f"{month}: N{total:.2f}")
        print(f"Overall Average: N{overall_average:.2f}")
    elif choice == "2":
        category_trends = analyze_category_trends(expenses)
        print("\nCategory Trends:")
        for category, trend in category_trends.items():
            print(f"{category}: {trend}")
    elif choice == "3":
        forecast_total, category_forecast = forecast_next_30_days(expenses)
        print(f"\nForecasted Expenses for Next 30 Days: N{forecast_total:.2f}")
        print("\nCategory Breakdown:")
        for category, forecast in category_forecast.items():
            print(f"{category}: N{forecast:.2f}")
    elif choice == "4":
        income = float(input("Enter your monthly income: "))
        saving_potential = calculate_saving_potential(expenses, income)
        print(f"\nSaving Potential: N{saving_potential:.2f}")
        print(f"Saving Percentage: {(saving_potential / income) * 100:.2f}%")
    elif choice == "5":
        print("Thank you for using the Spending Forecaster. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")