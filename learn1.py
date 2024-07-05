'''
    Write a Python program to classify a given number into one of three categories: negative, zero, or positive. The program should take an integer input and print out one of the following statements based on the input:
    "The number is negative." if the number is less than zero.
    "The number is zero." if the number is exactly zero.
    "The number is positive." if the number is more than zero.

    Example:
    Input: 3
    Output: The number is positive.
    Input: -5
    Output: The number is negative.
    Input: 0
    Output: The number is zero.
'''

num = int(input("Enter a number: "))
if (num > 1):
    print("The number is positive.")
elif (num < 1):
    print("The number is negative.")
elif (num == 0):
    print("The number is zero.")
else:
    print("Enter a valid input")

want_to_continue = input("Want to continue (y/n): ")
while (want_to_continue == 'y'):
    num = int(input("Enter a number: "))
    if (num > 1):
        print("The number is positive.")
    elif (num < 1 and num !=0):
        print("The number is negative.")
    elif (num == 0):
        print("The number is zero.")
    else:
        print("Enter a valid input")
    want_to_continue = input("Want to continue (y/n): ")
