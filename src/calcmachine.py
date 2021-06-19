#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################

from curtsies.fmtfuncs import cyan, magenta, red, bold, green

def main():
    while True:
        while True:
            base = input("Enter your first number: ").strip()
            if base.isalpha() or base == "" or not base.isalnum():
                print(red("Not a number!"))
            else:
                break
        while True:
            opr = input(f"Enter Operator {bold('([+] [-] [*] [/] [**] [//] [%])')}: ").strip()
            if opr == "+" or opr == "-" or opr == "*" or opr == "/" or opr == "**" or opr == "//" or opr == "%":
                break
            else:
                print(red("Wrong Operator!"))
        while True:
            nums = [i for i in input("Enter another number/s (n1,n2): ").strip().split(",")]
            fails = 0
            for num in nums:
                if num.isalpha() or num == "":
                    fails += 1
            if fails == 0:    
                break
            else:
                print(red("Can't calculate with non-numbers!"))

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