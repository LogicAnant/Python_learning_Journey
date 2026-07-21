age = int(input("Enter your age: "))
print("You are age is:", age)
# Conditional operators are used to compare values. The conditional operators are:
# == : equal to
# != : not equal to
# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to
if age >= 18:
    print("You are an adult.")
    print("so you are eligible to vote.")
else:
    print("You are not an adult.")
    print("so you are not eligible to vote.")

# there are elif statements in python which is used to check multiple conditions. The elif statement is short for else if. It allows you to check multiple conditions in a single if-else block. Here's an example:

num = int(input("Enter your marks: "))
if num >= 50 and num <= 60:
    print("good")
elif num >= 60 and num <= 70:
    print("very good")
elif num >= 70 and num <= 80:
    print("excellent")
elif num >= 80 and num <= 90:
    print("outstanding")
elif num >= 90 and num <= 100:
    print("topper")
else: 
    print("failed")  
print("You are good programmer")
                    