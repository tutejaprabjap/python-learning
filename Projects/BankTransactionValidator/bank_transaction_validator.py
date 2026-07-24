try:
    transaction_type = input("Enter transaction type (deposit/withdrawal):")
    amount = float(input("Enter transaction amount:"))

except ValueError:
    print("Invalid transaction amount. Please enter a numeric value.")

else:
    if transaction_type not in ["deposit", "withdrawal"]:
        print("Invalid transaction type.")
    elif amount <= 0:
        print("Transaction amount must be greater than $0.00.")
    elif amount > 10000:
        print("Transaction requires manager review.")
    else:
        print(f"{transaction_type.capitalize()} approved: ${amount:.2f}")

finally:
    print("Transaction validation complete.")





