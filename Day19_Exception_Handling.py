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
try:
    while True:
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        computer = random.choice(num)
        print("Guess the number betweeen 0-9")
        user = int(input("Enter your number: "))
        if user == computer:
            print("Correct! You won")
        else:
            print("Wrong number try again")
        quit = input("enter 'exit' to quit or press any key to continue: ")
        if quit == "exit":
            print("Game over")
            break
except:
    print("please enter a valid integer")