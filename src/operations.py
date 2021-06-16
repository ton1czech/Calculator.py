from curtsies.fmtfuncs import bold, green

def addition(opr, base, *nums):
    print(f"\n{base}", end="")
    res = base
    for num in nums:
        res += num
        print(f" {opr} {num}", end="")
    print(" = ", end="")
    print(bold(green(f"{res}\n")))

def subtraction(opr, base, *nums):
    print(f"\n{base}", end="")
    res = base
    for num in nums:
        res -= num
        print(f" {opr} {num}", end="")
    print(" = ", end="")
    print(bold(green(f"{res}\n")))

def multiplication(opr, base, *nums):
    print(f"\n{base}", end="")
    res = base
    for num in nums:
        res *= num
        print(f" {opr} {num}", end="")
    print(" = ", end="")
    print(bold(green(f"{res}\n")))

def division(opr, base, *nums):
    print(f"\n{base}", end="")
    res = base
    for num in nums:
        res /= num
        print(f" {opr} {num}", end="")
    print(" = ", end="")
    print(bold(green(f"{res}\n")))

def exponent(opr, base, num):
    print(f"\n{base} {opr} {num} = ", end="")
    print(bold(green(f"{base ** num}\n")))