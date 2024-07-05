num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
operation = input("Enter the operation: ")
if operation == '+':
    add = num1 + num2
    print("Sum is : ", add)
elif operation == '-':
    diff = num1 - num2
    print("Difference is : ", diff)
elif operation == '*':
    mul = num1 * num2
    print("Product is : ", mul)
elif operation == '/':
    quo = num1 / num2
    print("Quotient is : ", quo)
elif operation == '%':
    rem = num1 % num2
    print("Remainder is : ", rem)
else:
    print("Enter a valid operation input... ")
