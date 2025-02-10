import os
import matplotlib.pyplot as plt
from collections import defaultdict
from enum import Enum
import csv
from decimal import Decimal

OUTPUT_DIR = r'...\Report'

class DataRow:
    def __init__(self, row):
        self.U = row['u']
        self.F = row['f']
        self.Kernel = row['kernel']
        self.Lambda = row['lambda']

        self.UIsPolynomial = row['u_is_polynomial'].lower() == 'true'
        self.UIsTrigonometric = row['u_is_trigonometric'].lower() == 'true'
        self.UIsHyperbolic = row['u_is_hyperbolic'].lower() == 'true'
        self.UIsExponential = row['u_is_exponential'].lower() == 'true'
        self.UMaxDegree = Decimal(row['u_max_degree'])

        self.FIsPolynomial = row['f_is_polynomial'].lower() == 'true'
        self.FIsTrigonometric = row['f_is_trigonometric'].lower() == 'true'
        self.FIsHyperbolic = row['f_is_hyperbolic'].lower() == 'true'
        self.FIsExponential = row['f_is_exponential'].lower() == 'true'
        self.FMaxDegree = Decimal(row['f_max_degree'])

        self.KernelIsPolynomial = row['kernel_is_polynomial'].lower() == 'true'
        self.KernelIsTrigonometric = row['kernel_is_trigonometric'].lower() == 'true'
        self.KernelIsHyperbolic = row['kernel_is_hyperbolic'].lower() == 'true'
        self.KernelIsExponential = row['kernel_is_exponential'].lower() == 'true'
        self.KernelMaxDegree = Decimal(row['kernel_max_degree'])

        self.LambdaIsPolynomial = row['lambda_is_polynomial'].lower() == 'true'
        self.LambdaIsTrigonometric = row['lambda_is_trigonometric'].lower() == 'true'
        self.LambdaIsHyperbolic = row['lambda_is_hyperbolic'].lower() == 'true'
        self.LambdaIsExponential = row['lambda_is_exponential'].lower() == 'true'
        self.LambdaMaxDegree = Decimal(row['lambda_max_degree'])

class TypeOfExpression(Enum):
    RealValue = 1
    Polynomial = 2
    Trigonometric = 3
    Hyperbolic = 4
    Exponential = 5


TypeOfExpressionColors = {
    TypeOfExpression.RealValue: "#03045e",
    TypeOfExpression.Polynomial: "#0077b6",
    TypeOfExpression.Trigonometric: "#00b4d8",
    TypeOfExpression.Hyperbolic: "#669bbc",
    TypeOfExpression.Exponential: "#90e0ef"
}


def max_degrees(data_rows):
    max_degrees = [max(row.UMaxDegree, row.FMaxDegree, row.KernelMaxDegree, row.LambdaMaxDegree) for row in data_rows]

    result = defaultdict(int)
    for degree in max_degrees:
        result[degree] += 1

    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)[:10]

    xs, ys = zip(*sorted_result)

    plt.bar(xs, ys, color='blue')
    plt.title("Max Degree")
    plt.xlabel("Degree")
    plt.ylabel("Count")
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, 'MaxDegrees.png'), dpi=100)
    plt.clf()


def format_plot(data_rows, key_selector, plot_title):
    result = defaultdict(int)

    for row in data_rows:
        expression_type = key_selector(row)
        result[expression_type] += 1

    for type_of_expression in TypeOfExpression:
        if type_of_expression not in result:
            result[type_of_expression] = 0

    labels = [type_of_expression.name for type_of_expression in TypeOfExpression]
    sizes = [result[type_of_expression] for type_of_expression in TypeOfExpression]
    colors = [TypeOfExpressionColors[type_of_expression] for type_of_expression in TypeOfExpression]

    plt.pie(sizes, labels=None, colors=colors)
    plt.title(plot_title, fontweight='bold')
    plt.legend(labels, loc="upper right")
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, f'{plot_title}.png'), dpi=100)
    plt.clf()


def u_format(data_rows):
    format_plot(data_rows,
                lambda x: TypeOfExpression.Exponential if x.UIsExponential else
                TypeOfExpression.Trigonometric if x.UIsTrigonometric else
                TypeOfExpression.Hyperbolic if x.UIsHyperbolic else
                TypeOfExpression.Polynomial if x.UIsPolynomial else
                TypeOfExpression.RealValue,
                "UFormat")


def f_format(data_rows):
    format_plot(data_rows,
                lambda x: TypeOfExpression.Exponential if x.FIsExponential else
                TypeOfExpression.Trigonometric if x.FIsTrigonometric else
                TypeOfExpression.Hyperbolic if x.FIsHyperbolic else
                TypeOfExpression.Polynomial if x.FIsPolynomial else
                TypeOfExpression.RealValue,
                "FFormat")


def kernel_format(data_rows):
    format_plot(data_rows,
                lambda x: TypeOfExpression.Exponential if x.KernelIsExponential else
                TypeOfExpression.Trigonometric if x.KernelIsTrigonometric else
                TypeOfExpression.Hyperbolic if x.KernelIsHyperbolic else
                TypeOfExpression.Polynomial if x.KernelIsPolynomial else
                TypeOfExpression.RealValue,
                "KernelFormat")


def lambda_format(data_rows):
    format_plot(data_rows,
                lambda x: TypeOfExpression.Exponential if x.LambdaIsExponential else
                TypeOfExpression.Trigonometric if x.LambdaIsTrigonometric else
                TypeOfExpression.Hyperbolic if x.LambdaIsHyperbolic else
                TypeOfExpression.Polynomial if x.LambdaIsPolynomial else
                TypeOfExpression.RealValue,
                "LambdaFormat")


def read_csv(file_path):
    data_rows = []

    with open(file_path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            data_rows.append(DataRow(row))

    return data_rows


data_rows = read_csv(r'...\Fredholm_Dataset_Sample.csv')

max_degrees(data_rows)
u_format(data_rows)
f_format(data_rows)
kernel_format(data_rows)
lambda_format(data_rows)
