age = int(input("Enter your age: "))
print("1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday")
day = int(input("Enter Day: "))

if age < 13:
    price = 100
elif age >= 13 and age <= 60:
    price = 180
else:
    price = 120

if day == 6 or day == 7:
    price += 50

print(f"Price ticket: {price} bath")

    