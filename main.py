# Daniel Anthony Baudyš (ton1czech)
# 28 09 2020

import pygame
from pygame import mixer
import time
import os

# sounds
def coin():
    mixer.init()
    mixer.music.load('audio/coin.wav')
    mixer.music.play()
    time.sleep(1)

def fail():
    mixer.init()
    mixer.music.load('audio/fail.wav')
    mixer.music.play()
    time.sleep(1.5)

def laugh():
    mixer.init()
    mixer.music.load('audio/laugh.wav')
    mixer.music.play()
    time.sleep(7)

# variables
num1 = input('Enter First Number: ')
opr = input('Enter Operator|+|-|/|*|%|<>|: ')
num2 = input('Enter Second Number: ')

# 2 numbers
def plus_():
    plus = float(num1) + float(num2) 
    print(num1, '+', num2, '=', plus)
    coin()
def minus_():
    minus = float(num1) - float(num2)
    print(num1, '-', num2, '=', minus)
    coin()
def multiply_():
    multiply = float(num1) * float(num2)
    print(num1, '*', num2, '=', multiply)
    coin()
def divided_():
    divided = float(num1) / float(num2)
    print(num1, '/', num2, '=', divided)
    coin()
def percentage_():
    percentage = (int(num1) / int(num2)) * 100
    print(num1, 'of', num2, 'is', percentage, '%')
    coin()
def less_greater_():
    if (float(num1) < float(num2)):
            print(num1, "is less than", num2)
            coin()
    elif (float(num1) > float(num2)):
            print(num1, "is greater than", num2)
            coin()

answer = input('Do you want to add third number ? (y/n) ')

# 3 numbers
def plus_plus_():
    plus_plus = float(num1) + float(num2) + float(num3)
    print(num1, '+', num2, '+', num3, '=', plus_plus)
    coin()
def plus_minus_():
    plus_minus = float(num1) + float(num2) - float(num3)
    print(num1, '+', num2, '-', num3, '=', plus_minus)
    coin()
def plus_multiply_():
    plus_multiply = float(num1) + float(num2) * float(num3)
    print(num1, '+', num2, '*', num3, '=', plus_multiply)
    coin()
def plus_divided_():
    plus_divided = float(num1) + float(num2) / float(num3)
    print(num1, '+', num2, '/', num3, '=', plus_divided)
    coin()

def minus_plus_():
    minus_plus = float(num1) - float(num2) + float(num3)
    print(num1, '-', num2, '+', num3, '=', minus_plus)
    coin()
def minus_minus_():
    minus_minus = float(num1) - float(num2) - float(num3)
    print(num1, '-', num2, '-', num3, '=', minus_minus)
    coin()
def minus_multiply_():
    minus_multiply = float(num1) - float(num2) * float(num3)
    print(num1, '-', num2, '*', num3, '=', minus_multiply)
    coin()
def minus_divided_():
    minus_divided = float(num1) - float(num2) / float(num3)
    print(num1, '-', num2, '/', num3, '=', minus_divided)
    coin()

def multiply_plus_():
    multiply_plus = float(num1) * float(num2) + float(num3)
    print(num1, '*', num2, '+', num3, '=', multiply_plus)
    coin()
def multiply_minus_():
    multiply_minus = float(num1) * float(num2) - float(num3)
    print(num1, '*', num2, '-', num3, '=', multiply_minus)
    coin()
def multiply_multiply_():
    multiply_multiply = float(num1) * float(num2) * float(num3)
    print(num1, '*', num2, '*', num3, '=', multiply_multiply)
    coin()
def multiply_divided_():
    multiply_divided = float(num1) * float(num2) / float(num3)
    print(num1, '*', num2, '/', num3, '=', multiply_divided)
    coin()

def divided_plus_():
    divided_plus = float(num1) / float(num2) + float(num3)
    print(num1, '/', num2, '+', num3, '=', divided_plus)
    coin()
def divided_minus_():
    divided_minus = float(num1) / float(num2) - float(num3)
    print(num1, '/', num2, '-', num3, '=', divided_minus)
    coin()
def divided_multiply_():
    divided_multiply = float(num1) / float(num2) * float(num3)
    print(num1, '/', num2, '*', num3, '=', divided_multiply)
    coin()
def divided_divided_():
    divided_divided = float(num1) / float(num2) / float(num3)
    print(num1, '/', num2, '/', num3, '=', divided_divided)
    coin()

# operations
if answer == "n":
    if opr == "+":
        plus_()
    elif opr == "-":
        minus_()
    elif opr == "*":
        multiply_()
    elif opr == "/":
        divided_()
    elif opr == "%":
        percentage_()
    elif opr == "<>":
        less_greater_()
    else:
        print('Wrong operator !')
        fail()
        
elif answer == "y":
    opr2 = input('Enter Operator|+|-|/|*|: ')
    num3 = input('Enter Third Number: ')

    if ((num1 == "6") and (opr == "+") and (num2 == "6") and (opr2 == "+") and (num3 == "6")):
        print("666............. SEE YOU IN HELL      MUHAHAHAHAHA")
        laugh()

    elif ((opr == "+") and (answer == "y")):
        if  (opr2 == "+"):
            plus_plus_()
        elif (opr2 == "-"):
            plus_minus_()
        elif (opr2 == "*"):
            plus_multiply_()
        elif (opr2 == "/"):
            plus_divided_()
        else:
            print("Something is wrong !")
            fail()

    elif ((opr == "-") and (answer == "y")):
        if (opr2 == "+"):
            minus_plus_()
        elif (opr2 == "-"):
            minus_minus_()
        elif (opr2 == "*"):
            minus_multiply_()
        elif (opr2 == "/"):
            minus_divided_()
        else:
            print("Something is wrong !")
            fail()

    elif ((opr == "*") and (answer == "y")):
        if (opr2 == "+"):
            multiply_plus_()
        elif (opr2 == "-"):
            multiply_minus_()
        elif (opr2 == "*"):
            multiply_multiply_()
        elif (opr2 == "/"):
            multiply_divided_()
        else:
            print("Something is wrong !")
            fail()

    elif ((opr == "/") and (answer == "/")):
        if (opr2 == "+"):
            divided_plus_()
        if (opr2 == "-"):
            divided_minus_()
        if (opr2 == "*"):
            divided_multiply_()
        if (opr2 == "/"):
            divided_divided_()
        else:
            print("Something is wrong !")
            fail()
    else:
        print("Wrong operator !")
        fail()
else:
    print("Something is wrong !")
    fail()