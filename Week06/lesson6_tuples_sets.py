customer_ids = [
    "C1001",
    "C1002",
    "C1003",
    "C1004",
    "C1005",
    "C1002",
    "C1006",
    "C1007",
    "C1008",
    "C1003",
    "C1009",
    "C1010",
    "C1011",
    "C1005",
    "C1012",
    "C1013",
    "C1014",
    "C1008",
    "C1015",
    "C1010"
]
print("Customer Data Cleaner")
print()

print("Original Customer IDs:")
for customer_id in customer_ids:
    print(customer_id)
print()

print("Unique Customer IDs:")
unique_customer_ids = set(customer_ids)
for customer_id in unique_customer_ids:
    print(customer_id)
print()

print("Clean Customer List:")
clean_customer_ids = list(unique_customer_ids)
for customer_id in clean_customer_ids:
    print(customer_id)






website_customers = {
    "C1001",
    "C1002",
    "C1003",
    "C1004",
    "C1005"
}

mobile_customers = {
    "C1003",
    "C1004",
    "C1005",
    "C1006",
    "C1007"
}

all_customers = website_customers | mobile_customers
shared_customers = website_customers & mobile_customers
website_only = website_customers - mobile_customers
single_platform_customers = website_customers ^ mobile_customers

print("Customer Database Comparison")
print()
print("All Customers:")
print(all_customers)
print()
print("Shared Customers:")
print(shared_customers)
print()
print("Website Only:")
print(website_only)
print()
print("Single Platform Customers:")
print(single_platform_customers)
print()




employee = (
    "E1025",
    "Sarah Johnson",
    "Finance",
    75000
)

print("Employee Record")
print("---------------")
print(employee)
print()
print(f"Employee ID: {employee[0]}")
print(f"Department: {employee[2]}")
print()
employee_id, name, department, salary = employee
print("Unpacked Values")
print("---------------")
print(f"Employee ID: {employee_id}")
print(f"Name: {name}")
print(f"Department: {department}")
print(f"Salary: ${salary}")
