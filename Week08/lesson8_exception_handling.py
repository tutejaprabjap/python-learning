print("Bank Transaction Validator\n--------------------------")

try:
    amount = float(input("Enter transaction amount:"))

except ValueError:
    print("Invalid transaction amount. Please enter a numeric value.")

else:
    print(f"Transaction amount accepted: ${amount:.2f}")

finally:
    print("Transaction validation complete.")