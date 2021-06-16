#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################

import operations as op
from curtsies.fmtfuncs import cyan, magenta, red, bold



def calculate():
    while True:
        base = float(input("Enter your first number: "))
        opr = input(f"Enter Operator {bold('(+ - * / **)')}: ")

        nums = [float(i) for i in input("Enter another number/s (n1,n2): ").split(",")]

        if opr == '+':
            op.addition(opr, base, *nums)
        elif opr == '-':
            op.subtraction(opr, base, *nums)
        elif opr == '*':
            op.multiplication(opr, base, *nums)
        elif opr == '/':
            op.division(opr, base, *nums)
        elif opr == '**':
            op.exponent(opr, base, nums[0])
        else:
            print(red("Wrong Operator!"))

        more = input(magenta("Do you want to calculate more? (Y/n): "))
        if more == "n" or more == "no" or more == 'No':
            print(cyan("Sad to see you go. See you soon."))
            break

if __name__ == "__main__":
    calculate()