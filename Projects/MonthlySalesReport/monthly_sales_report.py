monthly_sales = [
    1250.50,
    980.75,
    1435.00,
    0,
    875.25,
    1620.40,
    1100.00,
    0,
    1349.80,
    950.60
]

def analyze_sales(sales):
    total_revenue = 0
    valid_sale_count = 0
    highest_sale = 0
    lowest_sale = None

    for sale in sales:
        if sale == 0:
            continue

        total_revenue += sale
        valid_sale_count += 1

        if sale > highest_sale:
            highest_sale = sale
        
        if lowest_sale is None or sale < lowest_sale:
            lowest_sale = sale
    
    average_sale = total_revenue / valid_sale_count

    return (
    total_revenue,
    valid_sale_count,
    highest_sale,
    lowest_sale,
    average_sale
)

total_revenue, valid_sale_count, highest_sale, lowest_sale, average_sale = analyze_sales(monthly_sales)

print("Monthly Sales Report")
print("--------------------")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Valid Sales: {valid_sale_count}")
print(f"Highest Sale: ${highest_sale:.2f}")
print(f"Lowest Sale: ${lowest_sale:.2f}")
print(f"Average Sale: ${average_sale:.2f}")

report = f"""Monthly Sales Report
--------------------
Total Revenue: ${total_revenue:.2f}
Valid Sales: {valid_sale_count}
Highest Sale: ${highest_sale:.2f}
Lowest Sale: ${lowest_sale:.2f}
Average Sale: ${average_sale:.2f}
"""

with open("monthly_sales_report.txt", "w") as file:
    file.write(report)
print("Monthly report saved successfully.")

with open("monthly_sales_report.txt","r") as file:
    saved_report = file.read()
print("Saved Report")
print("------------")
print(saved_report)