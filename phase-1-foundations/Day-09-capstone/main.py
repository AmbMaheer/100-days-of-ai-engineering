import analysis
import currency
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")

def generate_report():
    filename = "sales.csv"
    sales_data = analysis.load_sales_data(filename)
    
    if sales_data is None:
        print("Could not generate report: Data missing.")
        return

    total_rev = analysis.total_revenue(sales_data)
    total_profit, avg_profit_per_sale, profit_by_pkg = analysis.profit_summary(sales_data)
    avg_sale = total_rev / len(sales_data) if len(sales_data) > 0 else 0    
    packages = analysis.revenue_by_package(sales_data)
    best_package = packages.index[0] if not packages.empty else "N/A"
    
    customers = analysis.top_customers(sales_data, 1)
    top_customer_name = customers.index[0] if not customers.empty else "N/A"
    top_customer_spent = customers.iloc[0] if not customers.empty else 0
    total_unique_customers = sales_data['customer_name'].nunique()
    
    monthly_rev = analysis.revenue_by_month(sales_data)
    rates = currency.get_exchange_rates("USD", api_key)
    usd_val = currency.convert_currency(total_rev, "NGN", "USD", rates) if rates else 0
    eur_val = currency.convert_currency(total_rev, "NGN", "EUR", rates) if rates else 0
    gbp_val = currency.convert_currency(total_rev, "NGN", "GBP", rates) if rates else 0
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"============================================\n"
    report += f"   ELITE DATA SIM — DAILY INTELLIGENCE REPORT\n"
    report += f"   Generated: {current_time}\n"
    report += f"============================================\n\n"
    report += f"SALES SUMMARY\n"
    report += f"─────────────────────────────────────────\n"
    report += f"Total revenue:          N{total_rev:,.2f}\n"
    report += f"Total profit:           N{total_profit:,.2f}\n"
    report += f"Average sale value:     N{avg_sale:,.2f}\n"
    report += f"Best performing package: {best_package}\n\n"
    report += f"CUSTOMER INTELLIGENCE\n"
    report += f"─────────────────────────────────────────\n"
    report += f"Total customers:        {total_unique_customers}\n"
    report += f"Top customer:           {top_customer_name} (N{top_customer_spent:,.0f})\n\n"
    report += f"PACKAGE PROFIT MARGINS\n"
    report += f"─────────────────────────────────────────\n"
    if not profit_by_pkg.empty:
        for pkg_name, profit in profit_by_pkg.items():
            report += f"  - {pkg_name}: N{profit:,.2f}\n"
    else:
        report += "  No package data available.\n"
    report += f"\n"
    report += f"MONTHLY TREND\n"
    report += f"─────────────────────────────────────────\n"
    
    
    if not monthly_rev.empty:
        busiest_month = monthly_rev.idxmax()
        scale = 2000  
        for month, rev in monthly_rev.items():
            blocks = "█" * int(rev / scale)
            marker = "  ← busiest" if month == busiest_month else ""
            report += f"{month}    N{rev:,.0f}  {blocks}{marker}\n"
            
    report += f"\nCURRENCY SNAPSHOT (live rates)\n"
    report += f"─────────────────────────────────────────\n"
    report += f"Your N{total_rev:,.0f} revenue equals:\n"
    report += f"  USD:   ${usd_val:,.2f}\n"
    report += f"  EUR:   €{eur_val:,.2f}\n"
    report += f"  GBP:   £{gbp_val:,.2f}\n\n"
    
    report += f"============================================\n"
    print(report)
    

    save_report(report)

def save_report(report_text, folder="reports"):
    os.makedirs(folder, exist_ok=True)
    

    date_str = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(folder, f"report_{date_str}.txt")
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(report_text)
        
    print(f"Report saved to: {filepath}")
    print("============================================\n")

if __name__ == "__main__":
    generate_report()