#------------------
# Map function
#------------------

# The map() function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. 
def double(x):
    return x*2

l = [10, 15, 20, 25, 30]
doubled_list = list(map(double, l))
print(doubled_list)

#-----------------
# Filter function
#-----------------

# filter() funtion returns a boolen value.
def comparing(a):
    return a<20

newl = list(filter(comparing, l))
print(newl)

# reduce() function  argument is a function that takes in two arguments and returns a single value.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
