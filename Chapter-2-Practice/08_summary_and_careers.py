bill = float(input("Enter the total bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
people = int(input("Enter the number of people: "))
total_bill = bill + (bill * tip_percent / 100)
amount_per_person = total_bill / people
print(f"Each person pays: {amount_per_person:.2f}")
