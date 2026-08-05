#-------------------------------
# Short Hand if ... else (Ternary Operators)
#-------------------------------

a = 18 
b = 27
print("big brother") if a < b else print("small brother")

# Multiple conditions in one line
print(b) if a < b else print(a) if a > b else print("both are equal")


#----------------------
# Enumerate Function 
#----------------------

# Fix: Changed list variable name to plural 'countries'
countries = ['India', 'Mexico', 'Japan', 'Chicago']
for index, country in enumerate(countries):
    print(f"{index}. {country}")

# Starting the index at 1 using the 'start' argument
months = ('June', 'September', 'October')
for index, month in enumerate(months, start=1):
    print(index, month)

# Alternative manual index shifting (index + 1)
years = ('2012', '2008', '2026')
for index, year in enumerate(years):
    print(f"{index + 1}: {year}")
#-------------------------------
# Short Hand if ... else (Ternary Operators)
#-------------------------------

a = 18 
b = 27
print("big brother") if a < b else print("small brother")

# Multiple conditions in one line
print(b) if a < b else print(a) if a > b else print("both are equal")


#----------------------
# Enumerate Function 
#----------------------

# Fix: Changed list variable name to plural 'countries'
countries = ['India', 'Mexico', 'Japan', 'Chicago']
for index, country in enumerate(countries):
    print(f"{index}. {country}")

# Starting the index at 1 using the 'start' argument
months = ('June', 'September', 'October')
for index, month in enumerate(months, start=1):
    print(index, month)

# Alternative manual index shifting (index + 1)
years = ('2012', '2008', '2026')
for index, year in enumerate(years):
    print(f"{index + 1}: {year}")
