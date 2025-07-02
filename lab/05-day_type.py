print("1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday")
Day = int(input("Enter Day : "))
if Day <= 5:
    print("Weekday")
else:
    print("Weekend")