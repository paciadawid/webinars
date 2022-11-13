import math


class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    def odejmij(self, x, y):
        return x - y

    def multiple(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def inverted(self, x):
        return 1/x

    def factorial(self, x):
        return math.factorial(x)


cal = Calculator()

print(cal.add(1, 2))
print(cal.odejmij(1, 2))
print(cal.divide(1, 2))
print(cal.inverted(12345))
print(cal.factorial(3))

print(Calculator.add(1, 2))
