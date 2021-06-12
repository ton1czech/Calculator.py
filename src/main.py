#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################

### IMPORTS ###
import operations as op



### MECHANISM ###
def calculate():
    while True:
        base = float(input("Enter your first number: "))
        opr = input("Enter Operator (+ - * / **): ")

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
            print("Wrong Operator")

        more = input("Do you want to calculate more? (Y/n): ")
        if more == "n" or more == "no" or more == 'No':
            break

if __name__ == "__main__":
    calculate()