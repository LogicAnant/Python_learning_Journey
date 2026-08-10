#---------------------------
# Local vs Global Variables
#---------------------------

x = 5 #Global variable

def main():
    y = 20 #Local variable
    print(y)
main()
print(x)
# print(y) # this will throw an error because y is a local variable and is not accessible outside of the function.

# 'global' keyword help to access or change the value of globle variable.
a = 15
def new():
    global a
    a = 20
    print(a)
new()
print(a) # now the value of a has been changed.

#---------------
# File Handling
#---------------

# 'w' mode creates a new file if the already exits it throws exixt erorre.
n = open('myfile.txt', 'w')

# .write method is used to write the content in the file.
n.write("Python learning journey")
n.close() # close() method is used to close the file after opening it.

# open() function provide us to open a particuler file .
# it takes two arguments first one is name of file and second one is mode of file you want to open like 'r' for raeding, 'w' for writting, 'a' for appending.
# 'r' mode is default mode of file handling it is used to read the content of file. if we don't provide any mode it will open the file in 'r' mode.
n = open('myfile.txt')
print(n.read())
n.close()

# 'with' statement is used to open a file and it automatically closes the file after the block of code is executed.
with open('myfile.txt') as n:
    print(n.read())

