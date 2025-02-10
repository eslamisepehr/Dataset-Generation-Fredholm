import pandas as pd

# Define file paths for the three CSV files

dataset_dir = '...'
output_dir = '...'

file1 = dataset_dir + '01.csv'
file2 = dataset_dir + '02.csv'
file3 = dataset_dir + '03.csv'

# df1 = pd.read_csv(file1)
# df2 = pd.read_csv(file2)
# df3 = pd.read_csv(file3)
# combined_df = pd.concat([df1, df2, df3], ignore_index=True)
# combined_df.to_csv(output_dir + '\Fredholm_Full_Dataset.csv', index=False)

input_files = [file1, file2, file3]
with open(output_dir + '\\Fredholm_Full_Dataset.csv', 'w', encoding='utf-8') as outfile:
    for file in input_files:
        with open(file, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())