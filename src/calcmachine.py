#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################

import operations as op
from curtsies.fmtfuncs import cyan, magenta, red, bold



def calculate():
    while True:
        while True:
            base = None
            try:
                base = float(input("Enter your first number: "))
            except ValueError:
                print(red("Not a number"))
            if base:
                break
        while True:
            opr = input(f"Enter Operator {bold('(+ - * / **)')}: ")
            if opr == "+" or opr == "-" or opr == "*" or opr == "/" or opr == "**":
                break
            else:
                print(red("Wrong Operator!"))
        while True:
            nums = None
            try:
                nums = [float(i) for i in input("Enter another number/s (n1,n2): ").split(",")]
            except ValueError:
                print(red("Check your formatting. Something is wrong"))
            if nums:
                break

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

        more = input(magenta("Do you want to calculate more? (Y/n): ")).lower()
        if more == "n" or more == "no":
            print(cyan("Sad to see you go. See you soon."))
            break

if __name__ == "__main__":
    calculate()