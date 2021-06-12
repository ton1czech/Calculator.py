### OPERATIONS ###
def addition(opr, base, *nums):
    print(base, end="")
    res = base
    for num in nums:
        res += num
        print(f" {opr} {num}", end="")
    print(f" = {res}")

def subtraction(opr, base, *nums):
    print(base, end="")
    res = base
    for num in nums:
        res -= num
        print(f" {opr} {num}", end="")
    print(f" = {res}")

def multiplication(opr, base, *nums):
    print(base, end="")
    res = base
    for num in nums:
        res *= num
        print(f" {opr} {num}", end="")
    print(f" = {res}")

def division(opr, base, *nums):
    print(base, end="")
    res = base
    for num in nums:
        res /= num
        print(f" {opr} {num}", end="")
    print(f" = {res}")

def exponent(opr, base, num):
    print(f"{base} {opr} {num} = {base ** num}")