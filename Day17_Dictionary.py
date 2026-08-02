# ==========================================
# Day 17: Python Dictionaries Cheat Sheet
# ==========================================

# 1. Initialization & Printing
info = {'name': 'Vishal', 'age': 18, 'eligible': True}
print("Initial dictionary:", info)

# 2. Accessing Elements
print("Name:", info['name'])  
print("Age:", info['age'])

# Safe Accessing: .get() prevents KeyError if the key doesn't exist
print("Gender (Safe Access):", info.get('gender')) 

# 3. Viewing Collections
print("All Values:", info.values())
print("All Keys:", info.keys())
print("Key-Value Pairs:", info.items())

# 4. Modifying and Updating
info.update({'age': 19})
info.update({'DOB': 2008})
info['city'] = 'Delhi'  # Alternative clean direct assignment
print("Updated dictionary:", info)

# 5. Removing Elements
# pop() removes specified key and returns its value
rank = {'Vishal': 'A1', 'Kunal': 'A2', 'Mohit': 'A3'}
removed_rank = rank.pop('Vishal')
print("After pop():", rank)

# popitem() removes the last inserted pair
made_by = {'chair': 'wood', 'bottle': 'plastic', 'mirror': 'sand'}
removed_item = made_by.popitem()
print("After popitem():", made_by)

# del removes a specific item or the entire dictionary variable
del info['city']
print("After del key:", info)

# clear() flushes the entire dictionary structure
info.clear()
print("After clear():", info)

