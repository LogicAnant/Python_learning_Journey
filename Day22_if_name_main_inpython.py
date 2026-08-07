#---------------------------
# if __name__=="__main__"
#---------------------------

# The `if __name__ == "__main__":` construct in Python is used to determine whether a Python script is being run as the main program or if it is being imported as a module into another script.
def main():
    print("This code is running as the main program.")

if __name__ == "__main__":
    main()

# This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script. 
# For example, consider the following script:

def main():
    print("Running script directly")

if __name__ == "__main__":
    main()
# If you run this script directly, it will output "Running script directly". 
# However, if you import it as a module into another script and call the main function from the imported module, it will not output anything:

# import script
# script.main()  # Output: "Running script directly"

# This can be useful if you have code that you want to reuse in multiple scripts, 
# but you only want it to run when the script is run directly and not when it's imported as a module.