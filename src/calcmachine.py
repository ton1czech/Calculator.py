#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################

from curtsies.fmtfuncs import cyan, magenta, red, bold, green

def main():
    while True:
        while True:
            base = None
            try:
                base = input("Enter your first number: ")
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
                nums = [i for i in input("Enter another number/s (n1,n2): ").split(",")]
            except ValueError:
                print(red("Check your formatting. Something is wrong"))
            if nums:
                break

        calculate(opr, base, nums)

        more = input(magenta("Do you want to calculate more? (Y/n): ")).lower()
        if more == "n" or more == "no":
            print(cyan("Sad to see you go. See you soon."))
            break

def calculate(opr, base, *nums):
    print(f"\n{base}", end="")
    for num in nums[0]:
        base = base + opr + num
        res = eval(base)
        print(f" {opr} {num}", end="")
    print(" = ", end=""), print(bold(green(f"{res}\n")))

if __name__ == "__main__":
    main()