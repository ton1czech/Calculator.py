### OPERATIONS ###
def _addition(base_num, *nums):
    res = base_num
    for num in nums:
        res += num
    print(f"{res}")

def _subtraction(base_num, *nums):
    res = base_num
    for num in nums:
        res -= num
    print(f"{res}")

def _multiplication(base_num, *nums):
    res = base_num
    for num in nums:
        res *= num
    print(f"{res}")

def _division(base_num, *nums):
    res = base_num
    for num in nums:
        res /= num
    print(f"{res}")
