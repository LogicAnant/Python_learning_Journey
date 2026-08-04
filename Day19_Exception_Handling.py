#----------------------
# | Exception Handling |
#----------------------

# try...except blocks used to handle errors and exceptions.
# if try bock cathes error then the except block is executed.
try:
    num = int(input("Enter an integer: "))
except:  
    print("Number enterned is not an integer")

# Finally code block is always executed after try and except blocks, regardless of whether an exception occurred or not.
try:
    num = int(input("Enter your birth year: "))
    age = 2026 - num
    print("Your age is:", age)
except ValueError:
    print("enter your birth year not your name. please try again")
finally:
    print("Thanks for using my program")

# there are the number guessing game.
import random

print("--- Welcome to the Number Guessing Game ---")

while True:
    # Generate a random number between 0 and 9
    computer = random.randint(0, 9)
    print("\nGuess the number between 0-9")
    
    # Wrap only the risky input conversion inside the try block
    try:
        user = int(input("Enter your number: "))
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")
        continue  # Skips the rest of the loop and starts a new round
        
    # Check the guess
    if user == computer:
        print(f"🎉 Correct! The number was {computer}. You won!")
    else:
        print(f"😢 Wrong number. The computer chose {computer}. Try again!")
        
    # Ask to quit
    user_choice = input("Enter 'exit' to quit or press any key to continue: ").strip().lower()
    if user_choice == "exit":
        print("Game over. Thanks for playing!")
        break
