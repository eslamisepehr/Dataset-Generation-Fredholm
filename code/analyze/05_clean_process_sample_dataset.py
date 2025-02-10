import csv

### Variables

sample_path = r'...\Fredholm_Dataset_Sample.csv'

###

if __name__ == "__main__":

    header = [
            "u",
            "f",
            "kernel",
            "lambda",
            "a",
            "b",
            "u_is_polynomial", "u_is_trigonometric", "u_is_hyperbolic", "u_is_exponential", "u_max_degree",
            "f_is_polynomial", "f_is_trigonometric", "f_is_hyperbolic", "f_is_exponential", "f_max_degree",
            "kernel_is_polynomial", "kernel_is_trigonometric", "kernel_is_hyperbolic", "kernel_is_exponential", "kernel_max_degree",
            "lambda_is_polynomial", "lambda_is_trigonometric", "lambda_is_hyperbolic", "lambda_is_exponential", "lambda_max_degree"]

    data = []

    print("[*] Load Data")
    with open(sample_path, mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if "kernel" not in lines:
                data.append(lines)

    print(f"[*] Total Count: {len(data)}")

    unique_lists = [header]
    unique_lists.extend(list(map(list, set(map(tuple, data)))))

    print("[*] Save Data")
    with open(sample_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(unique_lists[:5001])
