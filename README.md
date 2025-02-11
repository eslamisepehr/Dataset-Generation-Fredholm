# Dataset Generation Fredholm

This repository contains the code for generating Fredholm second-kind equations, which are integral equations of the form:

$$
u(x) - \lambda \int_a^b K(x, t) u(t) dt = f(x)
$$

where $`K(x, t)`$ is the kernel function, $`\lambda`$ is a scalar parameter, and $`f(x)`$ is a given function.

This datasets can be useful for research in numerical analysis, machine learning, and applied mathematics.

The generated dataset is available on **Kaggle**, and the source code in this repository allows researchers to reproduce or modify the dataset according to their needs.

## Download Dataset

The dataset generated in this project is available in the `datasets` folder of this repository. You can access it using the link below:

[Go to the datasets folder](./datasets/)

## Usage

### 1. Install Dependencies

Before running the code, install the required Python packages. You can do this using the following command:

```bash
pip install -r requirements.txt
```

### 2. Running the Code
To generate the dataset, run:

```bash
python second_kind_Fredholm.py
```
