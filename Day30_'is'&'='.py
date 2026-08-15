#--------------
# 'is' and '='
#--------------

# is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

# for strings and integers, is and == will always return the same result:
x = "hello"
y = "hello"

print(x == y)  # True
print(x is y)  # True

p = 5
q = 5

print(p == q)  # True
print(p is q)  # True