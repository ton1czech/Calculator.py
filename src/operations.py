### OPERATIONS ###
def addition(base, *nums):
    res = base
    for num in nums:
        res += num
    print(f"{res}")

def subtraction(base, *nums):
    res = base
    for num in nums:
        res -= num
    print(f"{res}")

def multiplication(base, *nums):
    res = base
    for num in nums:
        res *= num
    print(f"{res}")

def division(base, *nums):
    res = base
    for num in nums:
        res /= num
    print(f"{res}")

def exponent(base, num):
    print(f"{base} ** {num} = {base ** num}")