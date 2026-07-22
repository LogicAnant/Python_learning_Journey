#there are objective questions in this program.(use of range() function)
print("Ques. How many colours in our flag ? ")
for x in range(1, 5):
    print(x)
option = int(input("Enter your answer: "))
if option == 3:
    print("Correct✅")
else:
    print("Wrong❌")
