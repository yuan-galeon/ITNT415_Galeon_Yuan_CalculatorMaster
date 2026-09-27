# Calculator Master
# Student: Yuan Galeon
# Course and Section: BIT41
# Feature branch: addition_Galeon


def addition(a, b):
    return a + b


def subtraction(a, b):
    pass


def multiplication(a, b):
    pass


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
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        print("Addition result:", addition(first, second))


if __name__ == "__main__":
    main()