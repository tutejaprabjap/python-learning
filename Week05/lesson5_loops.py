#Function
def process_sales(sales):
    total = 0

    for sale in sales:
        if sale == 0:
            continue

        total += sale
        print(f"Processed Sale: ${sale:.2f}")

    print(f"Total Sales: ${total:.2f}")


#Main Program
daily_sales = [125.50, 0, 89.75, 210.00, 0, 450.25]
process_sales(daily_sales)