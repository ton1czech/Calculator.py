#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################



### IMPORTS ###
# from operations import addition, subtraction, multiplication, division
import operations as op


### MECHANISM ###
base = float(input('Enter your first number: '))
opr = input('Enter Operator (+ - * / **): ')

nums = [float(i) for i in input("Enter another number/s (n1,n2): ").split(",")]

def calculate():
    if opr == '+':
        op.addition(base, *nums)
    elif opr == '-':
        op.subtraction(base, *nums)
    elif opr == '*':
        op.multiplication(base, *nums)
    elif opr == '/':
        op.division(base, *nums)
    elif opr == '**':
        op.exponent(base, nums[0])
    else:
        print("Wrong Operator")

if __name__ == "__main__":
    calculate()