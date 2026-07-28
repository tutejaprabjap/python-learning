
def calculate_profit(revenue, expenses):
    """Calculate and return the profit."""
    return revenue - expenses

def calculate_profit_margin(revenue, expenses):
    """Calculate and return the profit margin."""
    if revenue == 0:
        return 0 

    profit = calculate_profit(revenue,expenses)
    return (profit/revenue) * 100

def calculate_sales_tax(amount,tax_rate):
    """Calculate and return the sales tax on the amount."""
    return amount * tax_rate

def calculate_total_with_tax(amount, tax_rate):
    """Calculate and return the total with tax."""
    tax = calculate_sales_tax(amount,tax_rate)
    return amount + tax

def calculate_interest(principal, interest_rate=.05):
    """Calculate and return the interest earned."""
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    return principal * interest_rate
