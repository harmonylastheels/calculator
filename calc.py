def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "cannot divide by zero"
    return x / y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Choose (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Answer:", add(num1, num2))
        elif choice == '2':
            print("Answer:", subtract(num1, num2))
        elif choice == '3':
            print("Answer:", multiply(num1, num2))
        elif choice == '4':
            print("Answer:", divide(num1, num2))
    else:
        print("Invalid. Please try again.")

    again = input("Calculate more? (y/n): ")
    if again.lower() != 'y':
        break
