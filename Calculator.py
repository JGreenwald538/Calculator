import math


op = input("Enter operator:")

if op == "+":
    num1 = (input("Enter first number:"))
    num2 = (input("Enter second number:"))
    if num2 == "e":
        num2 = math.e
    if num2 == "pi":
        num2 = math.pi
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num3 = float(num1)+float(num2)
    print(str(num1) + " + " + str(num2) + " = " + str(num3))
elif op == "-":
    num1 = (input("Enter first number:"))
    num2 = (input("Enter second number:"))
    if num2 == "e":
        num2 = math.e
    if num2 == "pi":
        num2 = math.pi
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num3 = float(num1) - float(num2)
    print(str(num1) + " - " + str(num2) + " = " + str(num3))
elif op == "*":
    num1 = (input("Enter first number:"))
    num2 = (input("Enter second number:"))
    if num2 == "e":
        num2 = math.e
    if num2 == "pi":
        num2 = math.pi
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num3 = float(num1) * float(num2)
    print(str(num1) + " * " + str(num2) + " = " + str(num3))
elif op == "/":
    num1 = (input("Enter first number:"))
    num2 = (input("Enter second number:"))
    if num2 == "e":
        num2 = math.e
    if num2 == "pi":
        num2 = math.pi
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num3 = float(num1) / float(num2)
    print(str(num1) + " / " + str(num2) + " = " + str(num3))
elif op == "power":
    num1 = (input("Enter first number:"))
    num2 = (input("Enter second number:"))
    if num2 == "e":
        num2 = math.e
    if num2 == "pi":
        num2 = math.pi
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num3 = math.pow(float(num1), float(num2))
    print(str(num1) + "^" + str(num2) + " = " + str(num3))
elif op == "sqrt":
    num1 = (input("Enter a number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num2 = math.sqrt(float(num1))
    print("The square root of " + str(num1) + " is " + str(num2))
elif op == "exp":
    num1 = (input("Enter a number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num2 = math.exp(float(num1))
    print("e to the " + str(num1) + " power is " + str(num2))
elif op == "log":
    num1 = (input("Enter the constant number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num3 = math.log(float(num1))
    print("e to the " + str(num3) + " power gets you " + str(num1))
elif op == "log2":
    num1 = (input("Enter the constant number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num2 = math.log2(float(num1))
    print("2 to the " + str(num2) + " power gets you " + num1)
elif op == "log10":
    num1 = (input("Enter the constant number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num2 = math.log10(float(num1))
    print("10 to the " + str(num2) + " power gets you " + num1)
elif op == "sin":
    num1 = (input("Enter a number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num2 = math.sin(float(num1))
    num3 = math.degrees(num2)
    print("The sine of " + num1 + " is " + str(num2) + " in radians and " + str(num3) + " degrees")
elif op == "cos":
    num1 = (input("Enter a number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num2 = math.cos(float(num1))
    num3 = math.degrees(num2)
    print("The cosine of " + num1 + " is " + str(num2) + " in radians and " + str(num3) + " degrees")
elif op == "tan":
    num1 = (input("Enter a number:"))
    if num1 == "e":
        num1 = math.e
    if num1 == "pi":
        num1 = math.pi
    num2 = math.tan(float(num1))
    num3 = math.degrees(num2)
    print("The tangent of " + num1 + " is " + str(num2) + " in radians and " + str(num3) + " degrees")
else:
    print("Invalid Operator")

repeat = input("Would you like to repeat?:")
while repeat == "Yes":
    op = input("Enter operator:")
    if op == "+":
        num1 = (input("Enter first number:"))
        num2 = (input("Enter second number:"))
        if num2 == "e":
            num2 = math.e
        if num2 == "pi":
            num2 = math.pi
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num3 = float(num1) + float(num2)
        print(str(num1) + " + " + str(num2) + " = " + str(num3))
    elif op == "-":
        num1 = (input("Enter first number:"))
        num2 = (input("Enter second number:"))
        if num2 == "e":
            num2 = math.e
        if num2 == "pi":
            num2 = math.pi
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num3 = float(num1) - float(num2)
        print(str(num1) + " - " + str(num2) + " = " + str(num3))
    elif op == "*":
        num1 = (input("Enter first number:"))
        num2 = (input("Enter second number:"))
        if num2 == "e":
            num2 = math.e
        if num2 == "pi":
            num2 = math.pi
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num3 = float(num1) * float(num2)
        print(str(num1) + " * " + str(num2) + " = " + str(num3))
    elif op == "/":
        num1 = (input("Enter first number:"))
        num2 = (input("Enter second number:"))
        if num2 == "e":
            num2 = math.e
        if num2 == "pi":
            num2 = math.pi
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num3 = float(num1) / float(num2)
        print(str(num1) + " / " + str(num2) + " = " + str(num3))
    elif op == "power":
        num1 = (input("Enter first number:"))
        num2 = (input("Enter second number:"))
        if num2 == "e":
            num2 = math.e
        if num2 == "pi":
            num2 = math.pi
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num3 = math.pow(float(num1), float(num2))
        print(str(num1) + "^" + str(num2) + " = " + str(num3))
    elif op == "sqrt":
        num1 = (input("Enter a number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.sqrt(float(num1))
        print("The square root of " + str(num1) + " is " + str(num2))
    elif op == "exp":
        num1 = (input("Enter a number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.exp(float(num1))
        print("e to the " + str(num1) + " power is " + str(num2))
    elif op == "log":
        num1 = (input("Enter the constant number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.log(float(num1))
    elif op == "log2":
        num1 = (input("Enter the constant number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.log2(float(num1))
        print("2 to the " + str(num2) + " power gets you " + num1)
    elif op == "log10":
        num1 = (input("Enter the constant number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.log10(float(num1))
        print("10 to the " + str(num2) + " power gets you " + num1)
    elif op == "sin":
        num1 = (input("Enter a number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.sin(float(num1))
        num3 = math.degrees(num2)
        print("The sine of " + num1 + " is " + str(num2) + " in radians and " + str(num3) + " degrees")
    elif op == "cos":
        num1 = (input("Enter a number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.cos(float(num1))
        num3 = math.degrees(num2)
        print("The cosine of " + num1 + " is " + str(num2) + " in radians and " + str(num3) + " degrees")
    elif op == "tan":
        num1 = (input("Enter a number:"))
        if num1 == "e":
            num1 = math.e
        if num1 == "pi":
            num1 = math.pi
        num2 = math.tan(float(num1))
        num3 = math.degrees(num2)
        print("The tangent of " + num1 + " is " + str(num2) + " in radians and " + str(num3) + " degrees")
    else:
        print("Invalid Operator")
    repeat = input("Would you like to repeat?:")
if repeat != "Yes":
    print("Ok, thank you for calculating today!")
