transactions = [341.23, 85.33, 98.54, 54.45, 23.76]
print(f"Transactions today: {transactions}")

print(f"First Transaction: {transactions[0]:.2f}")
print(f"Last Transaction: {transactions[-1]:.2f}")

transactions.append(34.56)
transactions.insert(2, 56.87)

transactions.remove(85.33)

removed_transaction = transactions.pop()
print(f"Removed transaction: ${removed_transaction:.2f}")

transactions.sort()

for transaction in transactions:
    print(f"Updated Transactions today: ${transaction:.2f}")
