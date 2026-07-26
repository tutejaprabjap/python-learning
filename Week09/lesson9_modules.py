import financial_utils

amount = 500
discount_percent = .10

transaction_fee = financial_utils.calculate_transaction_fee(amount)
sales_tax = financial_utils.calculate_sales_tax(amount)
discounted_amount = financial_utils.apply_discount(amount,discount_percent)


print("Financial Utilities Demo\n------------------------")
print(f"Transaction Amount: ${amount:.2f}")
print(f"Transaction Fee: ${transaction_fee:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(
    f"Discounted Amount ({discount_percent * 100:.0f}%): "
    f"${discounted_amount:.2f}"
)