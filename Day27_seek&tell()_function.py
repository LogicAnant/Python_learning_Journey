# 1. Setup sample files
with open('file.txt', 'w') as f:
    f.write('abcdefghijklmnopqrstuvwxyz')

# 2. Demonstrating seek() and tell()
print("--- Seek and Tell ---")
with open('file.txt', 'r') as f:
    print(f"Start position: {f.tell()}")       # Output: 0
    
    first_read = f.read(10)
    print(f"Read first 10 characters: {first_read}")
    print(f"Position after read: {f.tell()}")    # Output: 10
    
    f.seek(5)                                    # Move pointer back to index 5
    print(f"Position after seek(5): {f.tell()}") # Output: 5
    print(f"Read from position 5: {f.read()}")   # Reads 'fgh...z'

# 3. Demonstrating truncate()
print("\n--- Truncate ---")
with open('sample.txt', 'w') as s:
    s.write('This is a sample text file.')
    s.truncate(7)                                # Truncate to first 7 bytes

with open('sample.txt', 'r') as s:
    print(f"Truncated content: {s.read()}")      # Output: 'This is'
