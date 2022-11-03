import pandas as pd
file = pd.read_csv("file-load.csv")
print(file.head())
print("=========================")
print(file.columns)
print("=========================")
print(file.tail())