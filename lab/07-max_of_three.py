num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
def find_max_number(n1, n2, n3):
    max_value = n1
    if n2 > max_value:
        max_value = n2
    if n3 > max_value:
        max_value = n3
    print(f"Max number {max_value}")

    
print(f"Max numbe {max(num1, num2, num3)}")