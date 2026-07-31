#This is the program to find next Febonacci number.

def Febonacci(num):
    if (num==0 or num==1):
        return 1
    else:
        return (num-1) + (num-2)
num = int(input("enter your number: "))
result = Febonacci(num)
print(f"Febonacci sequence is {result}")

#This is the program find out factorial number.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
i = int(input("enter your number: "))
result = factorial(i)
print(f"factorial number is {result}")