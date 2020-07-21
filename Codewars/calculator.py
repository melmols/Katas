# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division. For example, this should return 2, not 2.666666...:


def makeNum(num, func):
    if func == None:
        return num
    else:
        return func(num)


def zero(func=None):  # your code here
    return makeNum(0, func)


def one(func=None):  # your code here
    return makeNum(1, func)


def two(func=None):  # your code here
    return makeNum(2, func)


def three(func=None):  # your code here
    return makeNum(3, func)


def four(func=None):  # your code here
    return makeNum(4, func)


def five(func=None):  # your code here
    return makeNum(5, func)


def six(func=None):  # your code here
    return makeNum(6, func)


def seven(func=None):  # your code here
    return makeNum(7, func)


def eight(func=None):  # your code here
    return makeNum(8, func)


def nine(func=None):  # your code here
    return makeNum(9, func)


def plus(a):  # your code here
    def f(b):
        return (b + a)

    return f


def minus(a):  # your code here
    def f(b):
        return (b - a)

    return f


def times(a):  # your code here
    def f(b):
        return (b * a)

    return f


def divided_by(a):  # your code here
    def f(b):
        return int(b / a)

    return f


# Test.describe('Basic Tests')
# Test.assert_equals(seven(times(five())), 35)
# Test.assert_equals(four(plus(nine())), 13)
# Test.assert_equals(eight(minus(three())), 5)
# Test.assert_equals(six(divided_by(two())), 3)