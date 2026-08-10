# readlines() method reads the content of the file and returns a list of lines in the file.
f = open('myfile.txt', 'r')
while True:
    line = f.readlines()
    if not line:
        break
    print(line, end="")
f.close()

# writelines() method writs a sequence of strings to a file.
f = open('myfile.txt','w')
lines = ['LogicAnat is the besest channel for bca students.\n','We should to subscribe LogicAnat.\n']
f.writelines(lines)
print(type(lines))
f.close()

# # If you want to write multiple lines in sequence then you can use the for loop for it.
f = open('myfile.txt','w')
lines = ['line 1', 'line 2','line 3']
for line in lines:
    f.write(line)
f.close()
