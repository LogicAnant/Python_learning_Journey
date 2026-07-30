### Docstrings in python

#Python docstrings are strings used right after the definition of a function, method, class, or module. 
# They are used to document our code.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(n = int(input("enter your number: ")))
print(square.__doc__)

# PEP 8
#PEP 8 is a document that provides guidelines and best practices on how to write Python code. 
# It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. 
# The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# The Zen of Python
# Long time Pythoneer Tim Peters succinctly channels the BDFL’s guiding principles for Python’s design into 20 aphorisms, 
# only 19 of which have been written down.

import this