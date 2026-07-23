def main():
    print("Welcome to the simple menu program")
    print("1. Greet")
    print("2. Add two numbers")
    print("3. Check even/odd")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    match choice:
        case "1":
            name = input("Enter your name: ").strip()
            print(f"Hello, {name}! Nice to meet you.")
        case "2":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Sum:", a + b)
        case "3":
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print(number, "is even.")
            else:
                print(number, "is odd.")
        case "4":
            print("Goodbye!")
        case _:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
main()
