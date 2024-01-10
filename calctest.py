#code inspired by https://stackoverflow.com/questions/6881170/is-there-a-way-to-autogenerate-valid-arithmetic-expressions
from calculator import *

class Expression:
    pass

class Number(Expression):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

class BinaryExpression(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return str(self.left) + self.op + str(self.right)

class ParenthesizedExpression(Expression):
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return "(" + str(self.exp) + ")"

from random import random, randint, choice

def randomExpression(p = None):
    if p is None:
        p = random()

    if p > 1:
        return Number(randint(1, 100))
    elif randint(0, 1) == 0:
        return ParenthesizedExpression(randomExpression(p + 0.2))
    else:
        left = randomExpression(p + 0.2)
        op = choice(["+", "-", "*", "/"])
        right = randomExpression(p + 0.2)
        return BinaryExpression(left, op, right)

flag = True
for i in range(100):
    equation = str(randomExpression())
    if float(solve(modifyInput(equation))[0]) != float(eval(equation)):
        print("error")
        print(equation)
        print("my solve:", solve(modifyInput(equation))[0])
        print("eval solve:", eval(equation))
        flag = False
        break
if flag:
    print("no errors :D")

import unittest
class TestStringMethods(unittest.TestCase):

    def test_generic(self):
        equation = "3+2*(9/3)*2-1+7-1"
        self.assertEqual(float(solve(modifyInput(equation))[0]), float(eval(equation)))
        equation = "(1+(3*(2-(1))))"
        self.assertEqual(float(solve(modifyInput(equation))[0]), float(eval(equation)))
        equation = "4+1 - 2 * 6 + 4 * 4-5 + 3/2"
        self.assertEqual(float(solve(modifyInput(equation))[0]), float(eval(equation)))
unittest.main()