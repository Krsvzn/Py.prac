def sum(a,b):
    print(a+b)

def subtraction(a,b):
    print(a-b)

def multiplication(a,b):
    print(a*b)

def divison(a,b):
    print(a/b)

print("Welcome To The Calculator\n\n")
a = int(input("Enter The First Number -> "))
b = int(input("Enter The Second Number -> "))
operator = input("Enter The Operator(+,-,*,/) -> ")

if operator == "+":
    sum(a,b)

elif operator == "-":
    subtraction(a,b)

elif operator == "*":
    multiplication(a,b)

else:
    divison(a,b)
 
