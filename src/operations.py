### OPERATIONS ###
def _addition(base_num, *nums):
    res = base_num
    for num in nums:
        res += num
    print(f"{res}")
    __hell(res)

def _subtraction(base_num, *nums):
    res = base_num
    for num in nums:
        res -= num
    print(f"{res}")
    __hell(res)

def _multiplication(base_num, *nums):
    res = base_num
    for num in nums:
        res *= num
    print(f"{res}")
    __hell(res)

def _division(base_num, *nums):
    res = base_num
    for num in nums:
        res /= num
    print(f"{res}")
    __hell(res)

### EASTER EGGS ###
def __hell(res):
    if res == 666:
        print("See you in hell")
    else:
        pass