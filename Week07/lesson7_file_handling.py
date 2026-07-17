with open("daily_report.txt", "w") as file:
    file.write("Daily Sales Report\n------------------\nTotal Revenue: $950.50\nTransactions: 5\nHighest Sale: $450.25")
    
print("Daily report has been saved successfully.")

with open("daily_report.txt", "r") as file:
    contents = file.read()

print("Report Contents")
print("---------------")
print(contents)

with open("daily_report.txt", "a") as file:
    file.write("\nNew Sale Recorded: $275.00")

print("New sale has been added to the report.")

with open("daily_report.txt", "r") as file:
    contents = file.read()
print(contents)

