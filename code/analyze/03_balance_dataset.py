import random

### Variables

dataset_path = r'...\Fredholm_Dataset_Clean.csv'
dataset_balanced_path = r'...\Fredholm_Dataset.csv'

###

def search(data, keywords):

    result = []

    for line in data:
        for keyword in keywords:
            if keyword in line:
               result.append(line)

    return result


if __name__ == "__main__":

    lines = []
    data = []
    all_data = []

    with open(dataset_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    trigonometric_sign = ['sin', 'cos', 'tan', 'cot']
    trigonometric_result = search(lines, trigonometric_sign)
    random.shuffle(trigonometric_result)
    all_data.extend(trigonometric_result)
    data.extend(trigonometric_result[:390000])
    print("Total Trigonometric:", len(trigonometric_result))

    hyperbolic_sign = ['sinh', 'cosh', 'tanh', 'coth']
    hyperbolic_result = search(lines, hyperbolic_sign)
    random.shuffle(hyperbolic_result)
    all_data.extend(hyperbolic_result)
    data.extend(hyperbolic_result[:210000])
    print("Total Hyperbolic:", len(hyperbolic_result))

    exponential_sign = ['exp']
    exponential_result = search(lines, exponential_sign)
    random.shuffle(exponential_result)
    all_data.extend(exponential_result)
    data.extend(exponential_result[:210000])
    print("Total Exponential:", len(exponential_result))

    all_set = set(all_data)

    realValue_or_polynomial = []
    for line in lines:
        if line not in all_set:
            realValue_or_polynomial.append(line)

    data.extend(realValue_or_polynomial[:50000])
    print("Total Real Value or Polynomial:", len(realValue_or_polynomial))

    data_set = set(data)
    print("Total Data:", len(data_set))

    print("[*] Save")
    with open(dataset_balanced_path, 'w', encoding='utf-8') as file:
        file.write('u, f, kernel, lambda, a, b' + '\n')
        i = 0
        for item in data_set:
            if i == 500000 + 1:
                break

            file.write(item)
            i += 1