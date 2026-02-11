import math
x = int(input("please enter value x: "))
y = int(input("please enter value y: "))

op = input("what operation would you like to perform?, e.g., [+,-,*,/,sqrt] ")

if op == "+":
    z = x + y
    print("The addition is ",z)

elif op == "-":
    z = x - y
    print("The subtraction is ",z)

elif op == "*":
    z = x * y
    print("The product is ",z)

elif op == "/":
    z = x / y
    print("The division is ",z)
    
elif op == "sqrt":
    z = math.sqrt(x)
    print("The sqrt is  ",z)

else:
    print("Invalid operation, please try again")
