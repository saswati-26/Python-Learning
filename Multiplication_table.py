# WAP to print the multiplication table of the number input

num = int(input("Enter a number: "))
print(f"The multiplication table of {num} is : ")
for i in range (1,11):
    print (num, " * " ,i, " = " ,num*i)
