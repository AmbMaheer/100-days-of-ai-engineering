import analysis


print("===== ELITE DATA SIM — SALES REPORT =====")

filename = "sales.csv"
sales_data = analysis.load_sales_data(filename)
if sales_data is not None:
    total_revenue = analysis.total_revenue(sales_data)
    print(f"Total Revenue: ${total_revenue:,.2f}\n")
    print("Average sale value: ${:.2f}\n".format(total_revenue / len(sales_data)))
    print("Total profit: ${:,.2f}\n".format(total_revenue * 0.3))  # Assuming a profit margin of 30%

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
    print(revenue_by_month.to_string())

    busiest_month = revenue_by_month.idxmax()
    print(f"\nBusiest Month: {busiest_month}")
else:
    print("Failed to load sales data. Please check the file and try again.")

