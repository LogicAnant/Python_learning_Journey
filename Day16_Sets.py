# ==============================================================================
# Day 16: Python Sets
# Description: Mastering set operations, unique collections, and set methods.
# ==============================================================================

# Sets are unordered, mutable collections of unique items.
# Individual elements must be unchangeable (hashable), but the set itself can be modified.
s = {"LogicAnant", 15, 26, 11.11, "Vishal"}
print("Type of s:", type(s))

# Accessing set items using a loop
print("\n--- Iterating over Set ---")
for item in s:
    print(item)

# Creating a proper empty set (using {} creates an empty dictionary)
empty = set()
print("\nType of empty:", type(empty))

# ==============================================================================
# 1. JOINING SETS & MATHEMATICAL OPERATIONS
# ==============================================================================
s1 = {1, 2, 2, 7, 8}
s2 = {6, 5, 4, 2, 3}

# union() returns a NEW set with all unique elements from both sets
print("\nUnion:", s1.union(s2))

# update() adds items from another sequence into the EXISTING set in-place
s1.update(s2)
print("After update():", s1)

# intersection() returns a NEW set containing only common elements
country = {"India", "japan", "China", "korea"}
country2 = {"Pakistan", "India", "London", "Mexico"}
con3 = country.intersection(country2)
print("\nIntersection:", con3)

# intersection_update() modifies the original set to keep only common elements
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print("After intersection_update():", cities)

# symmetric_difference() returns a NEW set with elements NOT shared by both
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print("\nSymmetric Difference:", cities3)

# symmetric_difference_update() modifies the original set with uncommon elements
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print("After symmetric_difference_update():", cities)

# difference() returns a NEW set with elements only in the target set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print("\nDifference:", cities3)

# difference_update() modifies the original set directly by removing commonalities
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print("After difference_update():", cities)

# ==============================================================================
# 2. EVALUATION & BOOLEAN METHODS
# ==============================================================================
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("\nIs Disjoint?:", cities.isdisjoint(cities2))

# issuperset() checks if a set contains all elements of another set
cities3 = {"Tokyo", "Madrid", "Delhi"}
print("Is Superset?:", cities.issuperset(cities3))

# issubset() checks if all elements of a set belong to a target set
cities2 = {"Delhi", "Madrid"}
print("Is Subset?:", cities2.issubset(cities))

# ==============================================================================
# 3. MUTATING & DELETING ELEMENTS
# ==============================================================================
# add() inserts a single item
fav_series = {"Stanger Things", "Squid Game"}
fav_series.add("Alice in borderland")
print("\nAfter add():", fav_series)

# remove() deletes an item (Raises KeyError if the item is missing)
kdrama = {"Meeting you", "goblin", "My demon"}
kdrama.remove("Meeting you")
print("After remove():", kdrama)

# discard() deletes an item safely (Does NOT raise errors if missing)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Seoul")
print("After discard():", cities)

# pop() removes and returns an arbitrary element
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
popped_item = cities.pop()
print("After pop():", cities, f"| Removed item: {popped_item}")

# clear() flushes out all elements, leaving an empty set structure
trash = {"Recycle bin", "dust"}
trash.clear()
print("After clear():", trash)

# del completely removes the reference variable from memory
distraction = {"Mobile", "Instagram", "Scrolling"}
del distraction

# ==============================================================================
# 4. MEMBERSHIP TESTING
# ==============================================================================
info = {"Aliens", "Super power", "Magic", "Black Hole"}
if "Black Hole" in info:
    print("\nMembership Check: Black Hole exists")
else:
    print("\nMembership Check: Try in another set")

