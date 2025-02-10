import csv
import os
import random

import sympy as sp

### Variables

dataset_path = r'...\Fredholm_Dataset.csv'
sample_path = r'...\Fredholm_Dataset_Sample.csv'

###


def analyze(math_expression: str):
    expr = sp.sympify(math_expression)

    is_polynomial = expr.is_polynomial()
    is_trigonometric = expr.has(sp.sin, sp.cos, sp.tan, sp.cot)
    is_hyperbolic = expr.has(sp.sinh, sp.cosh, sp.cosh, sp.tanh, sp.coth)
    is_exponential = expr.has(sp.exp)

    max_degree = 1
    if is_polynomial:
        if len(expr.free_symbols) > 0:
            max_degree = float('-inf')
            for symbol in expr.free_symbols:
                degree = sp.degree(expr, symbol)
                if degree is not None:
                    max_degree = max(max_degree, degree)

    return (is_polynomial, is_trigonometric, is_hyperbolic, is_exponential, max_degree)


def calculate(row, output):
    u = row[0]
    f = row[1]
    kernel = row[2]
    _lambda = row[3]
    a = row[4]
    b = row[5]

    u_is_polynomial, u_is_trigonometric, u_is_hyperbolic, u_is_exponential, u_max_degree = analyze(u)
    f_is_polynomial, f_is_trigonometric, f_is_hyperbolic, f_is_exponential, f_max_degree = analyze(f)
    kernel_is_polynomial, kernel_is_trigonometric, kernel_is_hyperbolic, kernel_is_exponential, kernel_max_degree = analyze(
        kernel)
    lambda_is_polynomial, lambda_is_trigonometric, lambda_is_hyperbolic, lambda_is_exponential, lambda_max_degree = analyze(
        _lambda)

    result = [
        u, f, kernel, _lambda, a, b,
        u_is_polynomial, u_is_trigonometric, u_is_hyperbolic, u_is_exponential, u_max_degree,
        f_is_polynomial, f_is_trigonometric, f_is_hyperbolic, f_is_exponential, f_max_degree,
        kernel_is_polynomial, kernel_is_trigonometric, kernel_is_hyperbolic, kernel_is_exponential, kernel_max_degree,
        lambda_is_polynomial, lambda_is_trigonometric, lambda_is_hyperbolic, lambda_is_exponential, lambda_max_degree
    ]

    for r in result:
        if r is None or r == '':
            return

    print(','.join(map(str, result)), file=open(output, 'a'))




if __name__ == "__main__":
    print("[*] Loading Data")
    with open(dataset_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    print("[*] Total Length:", len(data))

    print("[*] shuffle Data")
    random.shuffle(data)

    print("[*] Analyzing Data")
    for i in range(0, len(data) - 1):
        row = data[i]
        print(i, ' - ', row)
        calculate(row, sample_path)

    print("[*] Done!")
