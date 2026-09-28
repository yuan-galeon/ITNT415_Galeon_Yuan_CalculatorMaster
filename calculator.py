# Calculator Master
# Student: Yuan Galeon
# Course and Section: BIT41

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def main():
    while True:
        print("\n=================================")
        print("       CALCULATOR MASTER")
        print("=================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print("=================================")

        choice = input("Choose an option: ")

        if choice == "5":
            print("Thank you for using Calculator Master!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select an option from 1 to 5.")
            continue

        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            if choice == "1":
                print("Addition result:", addition(first, second))

            elif choice == "2":
                print("Subtraction result:", subtraction(first, second))

            elif choice == "3":
                print("Multiplication result:", multiplication(first, second))

            elif choice == "4":
                if second == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Division result:", division(first, second))

        except ValueError:
            print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()