def calculate_transaction_fee(amount):
    return amount * .02

def calculate_sales_tax(amount):
    return amount * .07

def apply_discount(amount, discount_percent):
    return amount * (1 - discount_percent)