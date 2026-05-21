# Financial Calculator Main Program
# This program provides a command-line interface for users to perform various financial calculations.
import finance

print("Welcome to the Financial Calculator!")
while True:
    print("\nPlease select an option:")
    print("1. Calculate profit after tax")
    print("2. Calculate Return on Investment (ROI)")
    print("3. Calculate break-even point")
    print("4. Calculate compound interest")
    print("5. Summarize financial data")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        while True:            
            try:
                revenue = float(input("Enter the revenue: "))
                if revenue < 0:
                    print("Revenue cannot be negative. Please enter a valid revenue.")
                else:                    
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for revenue.")
        while True:           
            try:
                cost = float(input("Enter the cost: ")) 
                if cost < 0:
                    print("Cost cannot be negative. Please enter a valid cost.")
                else:
                    break 
            except ValueError:
                print("Invalid input. Please enter a valid number for cost.")
        while True:
                try:
                    tax_rate_input = float(input("Enter the tax rate (in %): "))
                    if tax_rate_input < 0:
                        print("Tax rate cannot be negative. Please enter a valid tax rate.")
                    else:
                        tax_rate = tax_rate_input / 100
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number for tax rate.")  
        
        profit = finance.calculate_profit(revenue, cost, tax_rate)
        print(f"The profit after tax is: N{profit:.2f}")

    elif choice == '2':
        while True:            
            try: 
                investment = float(input("Enter the investment amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for investment amount.")
        while True:
            try:
                returns = float(input("Enter the returns from the investment: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for returns.")
        roi = finance.calculate_roi(investment, returns)
        print(f"The ROI is: {roi:.2f}%")

    elif choice == '3':
        while True:
            try:
                fixed_costs = float(input("Enter the fixed costs: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for fixed costs.")
        while True:
            try:
                price_per_unit = float(input("Enter the selling price per unit: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for selling price per unit.")
        while True:
            try:
                cost_per_unit = float(input("Enter the variable cost per unit: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for variable cost per unit.")
        break_even_units = finance.calculate_break_even(fixed_costs, price_per_unit, cost_per_unit)
        print(f"The break-even point is: {break_even_units:.2f} units")

    elif choice == '4':
        while True:
            try:
                principal = float(input("Enter the principal amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for principal amount.")
        while True:
            try:
                rate = float(input("Enter the annual interest rate (in %): ")) / 100
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for interest rate.")
        while True:
            try:
                time = float(input("Enter the time in years: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for time.")
        while True:
            try:
                n = int(input("Enter the number of times interest is compounded per year: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the number of compounding periods.")
        amount = finance.calculate_compound_interest(principal, rate, time, n)
        print(f"The amount after compound interest is: N{amount:.2f}")

    elif choice == '5':
        transactions = []
        print("Enter financial transactions (negative values for expenses, positive for income; enter 0 to finish):")
        while True:
            transaction = float(input("Enter a transaction amount: "))
            if transaction == 0:
                break
            transactions.append(transaction)
            if len(transactions) == 0:
                print("No transactions were entered. Returning to menu.")
            else:
                summary = finance.summarize_finances(*transactions)
                print("Financial Summary:")
                print(f"Total Income: N{summary['total_income']:.2f}")
                print(f"Average Income: N{summary['average_income']:.2f}")
                print(f"Highest Income: N{summary['highest_income']:.2f}")
                print(f"Lowest Income: N{summary['lowest_income']:.2f}")
                print(f"Total Expenses: N{summary['total_expenses']:.2f}")
                print(f"Net Balance: N{summary['net_balance']:.2f}")

    elif choice == '6':
        print("Thank you for using the Financial Calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option (1-6).")
        continue