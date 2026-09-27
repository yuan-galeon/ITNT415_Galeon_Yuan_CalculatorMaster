# Calculator Master
# Student: Yuan Galeon
# Course and Section: BIT41
# Feature branch: addition_Galeon


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    pass


def main():
    print("=================================")
    print("       CALCULATOR MASTER")
    print("=================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=================================")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            print("Addition result:", addition(first, second))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == "2":
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            result = subtraction(first, second)
            print("Subtraction result:", result)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == "3":
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            result = multiplication(first, second)
            print("Multiplication result:", result)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()