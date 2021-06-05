#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################



### IMPORTS ###
from operations import addition, subtraction, multiplication, division


### MECHANISM ###
base = float(input('Enter your first number: '))
opr = input('Enter Operator (+ - * /): ')

nums = [float(i) for i in input("Enter another numbers (n1,n2): ").split(",")]

if opr == '+':
    addition(base, *nums)
elif opr == '-':
    subtraction(base, *nums)
elif opr == '*':
    multiplication(base, *nums)
elif opr == '/':
    division(base, *nums)
else:
    print("Wrong Operator")