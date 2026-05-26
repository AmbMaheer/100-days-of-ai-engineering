from calendar import month

import analysis

print("===== ELITE DATA SIM — SALES REPORT =====\n")

sales_data = analysis.load_sales_data("sales.csv")

if sales_data is not None:
    
    print(f"Total revenue:        N{analysis.total_revenue(sales_data):,.2f}")
    print(f"Average sale value:   N{analysis.average_sale_value(sales_data):,.2f}")
    total_profit, avg_profit, profit_by_pkg = analysis.profit_summary(sales_data)
    print(f"Total profit:         N{total_profit:,.2f}")
    print(f"Average profit/sale:  N{avg_profit:,.2f}")  # Display average profit per sale
    print("\nProfit by Package:")
    print(profit_by_pkg.to_string())
    revenue_by_package = analysis.revenue_by_package(sales_data)
    print("\nRevenue by Package:")
    print(revenue_by_package.to_string())
    print()

    top_customers = analysis.top_customers(sales_data)
    print("\nTop 5 Customers by Revenue:")
    print(top_customers.to_string())
    print()

    revenue_by_month = analysis.revenue_by_month(sales_data)
    print("\nRevenue by Month:")
    for month, revenue in revenue_by_month.items():
        print(f"  {month}    N{revenue:,.2f}")

    busiest = analysis.busiest_month(sales_data)
    print(f"\nBusiest Month: {busiest}")
else:
    print("Failed to load sales data. Please check the file and try again.")

