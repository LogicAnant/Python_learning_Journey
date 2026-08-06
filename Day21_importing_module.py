#------------------------------
# How import works in python
#------------------------------

# To import modules in python, we use the 'import' statement. it would be allow to use all the variables or a function in our current script.
import math
result = math.sqrt(9)
print(result)

# 'from' statement allows to use a specific function that would import from given module
from math import sqrt
result = sqrt(9)
print(result)

# '*' wildcard used to importing everything(all functions and variables) from given module by from statement.
from math import*
result = sqrt(9)
print(result)
print(pi)

# 'as' statement used to rename the imported module for short and easy to write.
import math as m 
result = m.pi
print(result)

# 'dir' function used to find all the function or variable into imported module.
print(dir(math))

# we can know the type of function defined in module.
result = math.pi
print(type(result))

