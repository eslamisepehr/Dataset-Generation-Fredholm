import os

### Variables

dataset_path = r'...\Fredholm_Dataset_Clean.csv' # Copy from Fredholm_Full_Dataset.csv

###


invalid_content = [
    "nan",
    "sign",
    "inf",
    "Integral",
    "and",
    "==",
    "!=",
    ">",
    "=>",
    "<=",
    "<",
    "if",
    "or",
    "I",
    "Pi",
    "Heaviside",
    "re",
    "im",
    "fresnelc",
    "Piecewise",
    "gamma",
    "hyper",
    "Lambda",
    "RootSum",
    "AccumBounds",
    "polylog",
    "zoo",
    "e+",
    "e-"
]


def is_valid(item):
    if not item or item.isspace() or len(item) > 100000:
        return False

    for invalid in invalid_content:
        if invalid.lower() in item.lower():
            return False

    return True


if __name__ == "__main__":
    if not os.path.exists(dataset_path):
        print(f"File not found: {dataset_path}")
        exit(1)

    with open(dataset_path, 'r') as file:
        lines = file.readlines()

    print("Total Lines:", len(lines))

    result = list({line.strip() for line in lines if is_valid(line)})

    with open(dataset_path, 'w') as file:
        file.write("\n".join(result))

    print("Total Cleaned Lines:", len(result))
