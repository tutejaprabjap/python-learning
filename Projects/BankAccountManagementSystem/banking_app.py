from bank_account import BankAccount, BusinessAccount, SavingsAccount

personal_account = BankAccount(
    "John Smith",
    "123456789",
    1500.00
)

savings_account = SavingsAccount(
    "Jake Jackson",
    "987654321",
    5000.00
)

business_account = BusinessAccount(
    "ABC Manufacturing",
    "192837465",
    50000.00
)

accounts = [
    personal_account,
    savings_account,
    business_account,
]

print(f"{BankAccount.bank_name}")
print("Account Management System")
print("-------------------------")
print()


print("Starting Balances")
print("-----------------")

for account in accounts:
    account.display_balance()

print()
print("Processing Transactions")
print("-----------------------")

print("Personal Account")
print("----------------")
personal_account.deposit(250.00)
personal_account.withdraw(100.00)

print()

print("Savings Account")
print("----------------")
savings_account.apply_interest()

print()

print("Business Account")
print("----------------")
business_account.withdraw(15000.00)

print()
print("Final Account Summary")
print("---------------------")

for account in accounts:
    account.display_balance()
