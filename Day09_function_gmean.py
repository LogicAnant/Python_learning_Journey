# Function to calculate the true Geometric Mean
def calculateGmean(a, b):
    gmean = (a * b) ** 0.5
    print(f"The Geometric Mean of {a} and {b} is: {gmean:.2f}")

# Example 1
a = 5
b = 10
calculateGmean(a, b)

# Example 2
c = 12
d = 14
calculateGmean(c, d)

# Multiplication table using a for loop
print("\n--- Multiples of 5 ---")
num = range(1, 11)
for x in num:
    print(f"5 x {x} = {5 * x}")
