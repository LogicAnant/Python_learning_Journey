### String formatting in python

# When we prefix the string with the letter 'f', the string becomes the f-string itself. 
# The f-string can be formatted in much same as the str.format() method. 
# The f-string offers a convenient way to embed Python expression inside string literals for formatting.

name = "Vishal Varma"
age = 18
country = "India"
print(f"Hi my name is {name}.\nI am {age} year old and i'am from {country}.")

price = 19.99999
print(f'your product price is {price:.2f}')

# In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them
# We can use it in a single statement as well.

print(f"for five products your price is {2 * 50}")
