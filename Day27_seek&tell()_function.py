#------------------
# seek() function
#------------------

# seek() function is used to change the current file position.
with open('file.txt', 'r') as f:
    print(f.read())
    f.seek(5) # Move the file pointer to the 5th byte in the file.
    print(f.read())

#------------------
# tell() function
#------------------

# tell() function is used to get the current file position.
    data = f.read(10)
    print(f"Current file position: {f.tell()}")

#------------------
# truncate() function
#------------------

# truncate() function is used to truncate the file to a specified size.
with open('sample.txt', 'w') as s:
    s.write('This is a sample text file.')
    s.truncate(5)
with open('sample.txt', 'r') as s:
    print(s.read())