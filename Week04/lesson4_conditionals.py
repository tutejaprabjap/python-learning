transaction = 900

if transaction > 1000:
    print("Executive Approval Required")
elif transaction > 500:
    print("Manager Approval Required")
else:
    print("Automatically Approved")


customer = "John"
purchase = 65
premium_member = True

if premium_member and purchase >= 100:
    print(f"{customer} qualifies for free shipping.")
else: 
    print("Shipping charges apply.")


verified = False

if not verified:
    print("Identity verification required.")


def evaluate_transaction(amount):
    if amount > 5000:
        print("Possible Fraud - Investigate Immediately")
    elif amount > 1000:
        print("Manager Review Required")
    else:
        print("Transaction Approved")

evaluate_transaction(250)
evaluate_transaction(1500)
evaluate_transaction(7000)
