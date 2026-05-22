
# finance.py
# This module provides financial calculation functions for the Financial Calculator application.

def calculate_profit(revenue, cost, tax_rate=0):
    """
    Calculate the profit after tax.

    Parameters:
    revenue (float): The total revenue.
    cost (float): The total cost.
    tax_rate (float): The tax rate as a decimal (e.g., 0.2 for 20%).

    Returns:
    float: The profit after tax.
    """
    gross_profit = revenue - cost
    tax_amount = gross_profit * tax_rate
    net_profit = gross_profit - tax_amount
    return net_profit


def calculate_roi(investment, returns):
    """
    Calculate the Return on Investment (ROI).

    Parameters:
    investment (float): The amount of money invested.
    returns (float): The amount of money returned from the investment.

    Returns:
    float: The ROI as a percentage.
    """
    if investment == 0:
        return 0
    roi = (returns - investment) / investment * 100
    return roi


def calculate_break_even(fixed_costs, price_per_unit, cost_per_unit):
    """
    Calculate the break-even point in units.

    Parameters:
    fixed_costs (float): The total fixed costs.
    price_per_unit (float): The selling price per unit.
    cost_per_unit (float): The variable cost per unit.

    Returns:
    float: The break-even point in units.
    """
    if price_per_unit <= cost_per_unit:
        return float('inf')  # Break-even point is infinite if price is less than or equal to cost
    break_even_units = fixed_costs / (price_per_unit - cost_per_unit)
    return break_even_units


def calculate_compound_interest(principal, rate, time, n=12):
    """
    Calculate the compound interest.

    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
    time (float): The time the money is invested for in years.
    n (int): The number of times that interest is compounded per year.

    Returns:
    float: The amount of money accumulated after n years, including interest.
    """
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

def summarize_finances(*transactions):
    """
    Summarize a list of financial transactions.

    Parameters:
    *transactions (float): A variable number of financial transactions (positive for income, negative for expenses).

    Returns:
    dict: A summary of total income, total expenses, and net balance.
    """
    total_income = sum(t for t in transactions if t > 0)
    average_income = total_income / len([t for t in transactions if t > 0]) if total_income > 0 else 0
    highest_income = max((t for t in transactions if t > 0), default=0)
    lowest_income = min((t for t in transactions if t > 0), default=0)
    total_expenses = sum(t for t in transactions if t < 0)
    net_balance = total_income + total_expenses
    return {
        'total_income': total_income,
        'average_income': average_income,
        'highest_income': highest_income,
        'lowest_income': lowest_income,
        'total_expenses': total_expenses,
        'net_balance': net_balance
    }