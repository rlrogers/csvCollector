import os
import pandas as pd

# store the categories of csvs
csv_01 = []
csv_02 = []
csv_03 = []

# Path of the main directory which houses the directory of csv files 
path = os.path.join('C:\\Users\\')

# files traverses through the main directory, may need to alter for loop depending on folder structure 
files = [os.path.join(path, dir, file) for dir, dir_name, file_list in os.walk(path) for file in file_list]
for file in files:
    if file.endswith('1.csv'):
        csv_01.append(file)
    elif file.endswith('2.csv'):
        csv_02.append(file)
    elif file.endswith('3.csv'):
        csv_03.append(file)

# concat csvs can always add specific destination
df_01 = pd.concat([pd.read_csv(f) for f in csv_01])
df_01.to_csv("merged_csv_01.csv")

df_02 = pd.concat([pd.read_csv(f) for f in csv_02])
df_02.to_csv("merged_csv_02.csv")

df_03 = pd.concat([pd.read_csv(f) for f in csv_03])
df_03.to_csv("merged_csv_03.csv")

# To test print
# print(csv_01)
# print(csv_02)
# print(csv_03)
