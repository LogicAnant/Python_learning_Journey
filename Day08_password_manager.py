saved_password = ""

def password():
    global saved_password
    print("--- Setup Your Account ---")
    saved_password = input("Set your new master password: ")
    print("Password set successfully!\n")
    print("1. Check your password")
    print("2. Login")
    print("3. Reset your password")
    print("4. Exit")
    
    try:
        number = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1-4.")
        return

    match number:
        case 1:
            check = input("Enter your password to check: ")
            match check:
                case _ if check == saved_password:
                    print("Password is correct.")
                    print("Your password is:", saved_password)
                case _:
                    print("Incorrect password.")
        case 2:
            login = input("Enter your password to login: ")
            match login:
                case _ if login == saved_password:
                    print("Login successful.")
                case _:
                    print("Incorrect password. Please try again.")
        case 3:
            reset = input("Enter your current password to reset: ")
            match reset:
                case _ if reset == saved_password:
                    new_password = input("Enter your new password: ")
                    saved_password = new_password 
                    print("Password reset successfully!")
                case _:
                    print("Incorrect current password. Cannot reset.")
        case 4:
            print("Exiting the program. Goodbye!")
        case _:
            print("Invalid choice. Please enter a number between 1-4.")

password()

