#Functions
def welcome_message():
    print("Welcome to the Transaction Summary System!")

def display_transaction(customer, amount):
    print(f"{customer} spent ${amount:.2f}")

def calculate_total(transactions):
    return sum(transactions)

#Main Program
welcome_message()

display_transaction("Billy",34.532)
display_transaction("Amy", 45.43)
display_transaction("Robert", 27.45)

transactions = [34.56, 52.67, 384.56, 66.35, 95.43]
total_sales = calculate_total(transactions)
print(f"Total Sales: ${total_sales:.2f}")