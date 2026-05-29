import datetime

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
        
    return savings, savings_percentage, monthly_totals, average_monthly_expense