#Function
def generate_sales_report(sales):
    total_revenue = 0
    valid_transaction_count = 0
    highest_sale = 0
    lowest_sale = None

    for sale in sales:
        if sale == 0:
            continue
    
        total_revenue += sale
        valid_transaction_count += 1

        if sale > highest_sale:
            highest_sale = sale
    
        if lowest_sale is None or sale < lowest_sale:
            lowest_sale = sale
    if valid_transaction_count > 0:
        average_sale = total_revenue/valid_transaction_count
    else:
        average_sale = 0
    print("==============================")
    print("      DAILY SALES REPORT      ")
    print("==============================")
    print()
    print(f"Total Revenue: ${total_revenue:.2f}")
    print(f"Valid Transactions: {valid_transaction_count}")
    print(f"Highest Sale: ${highest_sale:.2f}")
    print(f"Lowest Sale: ${lowest_sale:.2f}")
    print(f"Average Sales: ${average_sale:.2f}")
    print()
    print("Processed Sales")
    print("---------------")
    sale_number = 1
    for sale in sales:
        if sale == 0:
            continue
        print(f"Sale #{sale_number}: ${sale:.2f}")
        sale_number += 1
        

#Main Program
daily_sales = [125.50, 0, 89.75, 210.00, 450.25, 0, 75.00]
generate_sales_report(daily_sales)


