from scipy.integrate import quad
from random import random
from tqdm import tqdm
from math import *
import csv

class MathFunction:
    def __init__(self, function_str: str, function, function_range: tuple):
        self.function_str = function_str
        self.function = function
        self.function_range = function_range

    def trap_reimann(self, a_start: float, b_end: float, increments: int, debug=False) -> float:
        total = 0
        x_delta = (b_end - a_start) / increments

        if debug:
            print("X_delta", x_delta)
            print([a_start + x * x_delta for x in range(increments + 1)])

        for current_index in [a_start + x * x_delta for x in range(increments + 1)]:
            if current_index == a_start or current_index == b_end:
                total += self.function(current_index)
            else:
                total += self.function(current_index) * 2

            if debug:
                print("current index", current_index)
                print("function", self.function(current_index))
                print("total", total)

        if debug:
            print("total", total)
            print("x delta * total", x_delta * total)
            print("final", x_delta * total / 2)

        return x_delta * total / 2

    def get_data_frame(self) -> list:
        start, end = self.get_random_range()

        return [self.function_str, start, end] + [self.trap_reimann(start, end, int(pow(2, x))) for x in range(7)] + [quad(self.function, start, end)[0]]

    def get_random_range(self) -> tuple:
        n1 = self.function_range[0] + random() * (self.function_range[1] - self.function_range[0])
        n2 = self.function_range[0] + random() * (self.function_range[1] - self.function_range[0])

        return n1, n2


def generate_data(file_name: str, math_functions: list) -> None:
    fields = ['function name', 'start', 'end', 'increment1', 'increment2',
              'increment4', 'increment8', 'increment16', 'increment32',
              'increment 4', 'actual']

    with open(file_name, "w+", newline="") as file:
        csvwriter = csv.writer(file)

        csvwriter.writerow(fields)

        for math_function in tqdm(math_functions):
            for x in range(10):
                csvwriter.writerow(math_function.get_data_frame())


if __name__ == "__main__":
    integration_functions = [
        # Function, Lambda Function, Limits of Integration
        MathFunction("1", lambda x: 1, (-100, 100)),
        MathFunction("x", lambda x: x, (-100, 100)),
        MathFunction("x^2", lambda x: x ** 2, (-100, 100)),
        MathFunction("x^3", lambda x: x ** 3, (-100, 100)),
        MathFunction("sqrt(x)", lambda x: sqrt(x), (0, 100)),
        MathFunction("sin(x)", lambda x: sin(x), (-100, 100)),
        MathFunction("cos(x)", lambda x: cos(x), (-100, 100)),
        MathFunction("exp(x)", lambda x: exp(x), (-100, 100)),
        MathFunction("log(x)", lambda x: log(x), (0.01, 100)),
        MathFunction("1/x", lambda x: 1 / x, (0.01, 100)),
        MathFunction("tan(x)", lambda x: tan(x), (-pi / 4, pi / 4)),
        MathFunction("log(1+x)", lambda x: log(1 + x), (-.99, 1)),
        MathFunction("exp(-x^2)", lambda x: exp(-x ** 2), (-100, 100)),
        MathFunction("sqrt(1-x^2)", lambda x: sqrt(1 - x ** 2), (-0.99, 0.99)),
        MathFunction("abs(x)", lambda x: abs(x), (-100, 100)),
        MathFunction("x^(-0.5)", lambda x: x ** (-0.5), (0.01, 100)),
        MathFunction("exp(-x)", lambda x: exp(-x), (-100, 100)),
        MathFunction("sin(1/x)", lambda x: sin(1 / x), (0.01, 100)),
        MathFunction("cos(1/x)", lambda x: cos(1 / x), (0.01, 100)),
        MathFunction("tan(1/x)", lambda x: tan(1 / x), (0.75, 10)),
        MathFunction("sqrt(1+x^2)", lambda x: sqrt(1 + x ** 2), (-100, 100)),
        MathFunction("sqrt(1-x^2)+x", lambda x: sqrt(1 - x ** 2) + x, (-0.99, 0.99)),
        MathFunction("log(2*x)", lambda x: log(2 * x), (0.1, 100)),
        MathFunction("sin(x)*cos(x)", lambda x: sin(x) * cos(x), (-100, 100)),
        MathFunction("x*sin(x)", lambda x: x * sin(x), (-100, 100)),
        MathFunction("x*cos(x)", lambda x: x * cos(x), (-100, 100)),
        MathFunction("x*exp(x)", lambda x: x * exp(x), (-100, 100)),
        MathFunction("x*sqrt(x)", lambda x: x * sqrt(x), (0, 100)),
        MathFunction("sin(x^2)", lambda x: sin(x ** 2), (-100, 100)),
        MathFunction("cos(x^2)", lambda x: cos(x ** 2), (-100, 100)),
        MathFunction("exp(-x^2/2)", lambda x: exp(-x ** 2 / 2), (-100, 100)),
        MathFunction("sqrt(1-sin(x)^2)", lambda x: sqrt(1 - sin(x) ** 2), (-100, 100)),
        MathFunction("x^2*exp(-x)", lambda x: x ** 2 * exp(-x), (-100, 100)),
        MathFunction("x*log(1+x)", lambda x: x * log(1 + x), (-.99, 100)),
        MathFunction("x*sqrt(1-x^2)", lambda x: x * sqrt(1 - x ** 2), (-0.99, 0.99)),
        MathFunction("x*exp(-x^2)", lambda x: x * exp(-x ** 2), (-100, 100)),
        MathFunction("sin(x)+cos(x)", lambda x: sin(x) + cos(x), (-100, 100)),
        MathFunction("sin(x)-cos(x)", lambda x: sin(x) - cos(x), (-100, 100)),
        MathFunction("sin(x+1)+cos(x)", lambda x: sin(x + 1) + cos(x), (-100, 100)),
        MathFunction("sin(x)*exp(x)", lambda x: sin(x) * exp(x), (-100, 100)),
        MathFunction("cos(x)*exp(x)", lambda x: cos(x) * exp(x), (-100, 100)),
        MathFunction("sin(x)*x", lambda x: sin(x) * x, (-100, 100)),
        MathFunction("cos(x)*x", lambda x: cos(x) * x, (-100, 100)),
        MathFunction("exp(x)*x", lambda x: exp(x) * x, (-100, 100)),
        MathFunction("sin(x)*cos(x)*x", lambda x: sin(x) * cos(x) * x, (-100, 100)),
        MathFunction("sin(x)*exp(x)*x", lambda x: sin(x) * exp(x) * x, (-100, 100)),
        MathFunction("cos(x)*exp(x)*x", lambda x: cos(x) * exp(x) * x, (-100, 100)),
        MathFunction("x*sin(x)^2", lambda x: x * sin(x) ** 2, (-100, 100)),
        MathFunction("2*x**7 + 3*x**6 - 5*x**5 + 4*x**4 - 2*x**3 + x**2 - 3*x + 1", lambda x: 2 * x ** 7 + 3 * x ** 6 - 5 * x ** 5 + 4 * x ** 4 - 2 * x ** 3 + x ** 2 - 3 * x + 1, (-100, 100)),
        MathFunction("-x**7 + 2*x**6 - 4*x**5 + 3*x**4 + x**3 - 2*x**2 + 5*x - 1", lambda x: -x ** 7 + 2 * x ** 6 - 4 * x ** 5 + 3 * x ** 4 + x ** 3 - 2 * x ** 2 + 5 * x - 1, (-100, 100)),
        MathFunction("4*x**6 + x**5 - 3*x**4 + 2*x**3 + 5*x**2 - 2*x + 6", lambda x: 4 * x ** 6 + x ** 5 - 3 * x ** 4 + 2 * x ** 3 + 5 * x ** 2 - 2 * x + 6, (-100, 100)),
        MathFunction("-3*x**6 + 2*x**5 + 5*x**4 - 4*x**3 + x**2 - 3*x + 2", lambda x: -3 * x ** 6 + 2 * x ** 5 + 5 * x ** 4 - 4 * x ** 3 + x ** 2 - 3 * x + 2, (-100, 100)),
        MathFunction("x**6 - 2*x**5 + 3*x**4 - 5*x**3 + 4*x**2 - 2*x + 1", lambda x: x ** 6 - 2 * x ** 5 + 3 * x ** 4 - 5 * x ** 3 + 4 * x ** 2 - 2 * x + 1, (-100, 100)),
        MathFunction("2*x**5 - 4*x**4 + 5*x**3 + 3*x**2 - 2*x + 1", lambda x: 2 * x ** 5 - 4 * x ** 4 + 5 * x ** 3 + 3 * x ** 2 - 2 * x + 1, (-100, 100)),
        MathFunction("-x**5 + 3*x**4 - 2*x**3 + 4*x**2 - 3*x + 2", lambda x: -x ** 5 + 3 * x ** 4 - 2 * x ** 3 + 4 * x ** 2 - 3 * x + 2, (-100, 100)),
        MathFunction("5*x**4 + 2*x**3 - 3*x**2 + 4*x - 1", lambda x: 5 * x ** 4 + 2 * x ** 3 - 3 * x ** 2 + 4 * x - 1, (-100, 100)),
        MathFunction("-4*x**4 + 2*x**3 + x**2 - 3*x + 1", lambda x: -4 * x ** 4 + 2 * x ** 3 + x ** 2 - 3 * x + 1, (-100, 100)),
        MathFunction("2*x**3 + x**2 - 4*x + 3", lambda x: 2 * x ** 3 + x ** 2 - 4 * x + 3, (-100, 100)),
        MathFunction("-3*x**3 + 4*x**2 - 5*x + 2", lambda x: -3 * x ** 3 + 4 * x ** 2 - 5 * x + 2, (-100, 100)),
        MathFunction("x**3 - 2*x**2 + 3*x - 4", lambda x: x ** 3 - 2 * x ** 2 + 3 * x - 4, (-100, 100)),
        MathFunction("-4*x**3 + 3*x**2 + 2*x - 1", lambda x: -4 * x ** 3 + 3 * x ** 2 + 2 * x - 1, (-100, 100)),
        MathFunction("5*x**2 - 3*x + 2", lambda x: 5 * x ** 2 - 3 * x + 2, (-100, 100)),
        MathFunction("-2*x**2 + 4*x - 1", lambda x: -2 * x ** 2 + 4 * x - 1, (-100, 100)),
        MathFunction("3*x**2 + 2*x - 5", lambda x: 3 * x ** 2 + 2 * x - 5, (-100, 100)),
        MathFunction("x**2 - 4*x + 3", lambda x: x ** 2 - 4 * x + 3, (-100, 100)),
        MathFunction("-3*x**2 + 2*x + 1", lambda x: -3 * x ** 2 + 2 * x + 1, (-100, 100))
    ]
    generate_data("output.csv", integration_functions)
