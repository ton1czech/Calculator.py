#####################################
# Daniel Anthony Baudyš (ton1czech) #
# 28 09 2020                        #
#####################################



### IMPORTS ###
from operations import _addition, _subtraction, _multiplication, _division
from audio.audio import s_coin, s_fail, s_laugh



### MECHANISM ###
base_number = float(input('Enter your first number: '))
opr = input('Enter Operator (|+|-|*|/|): ')

numbers = input("Enter another numbers (n1,n2): ").split(",")
numbers = [float(i) for i in numbers]

if opr == '+':
    _addition(base_number, *numbers)
elif opr == '-':
    _subtraction(base_number, *numbers)
elif opr == '*':
    _multiplication(base_number, *numbers)
elif opr == '/':
    _division(base_number, *numbers)
else:
    print("Wrong Operator")