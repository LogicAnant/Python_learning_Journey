#------------------
# Lambda function
#------------------

# Lambda functions are anonymous functions in Python that can have any number of arguments but only one expression.
# They are often used for short, simple operations.

# Function to double the input
def double(x):
    return x*2
print(double(5))

# Lambda function to square the input
square = lambda x: x*x
print(square(5))

# It does'nt need a name
print((lambda a: a*a*a)(2))

# It can be take multiple argument
add = lambda x,y,z: x + y + z
print(add(5,3,6)) 

# Lambda function can also include multiple statements, but they are limited to a single expression.
lambda p,q: print(f"{p} * {q} = {p * q}")

# It can also use as a argument
def main(t):
    return t*t
print(main(add(5,6,2)))