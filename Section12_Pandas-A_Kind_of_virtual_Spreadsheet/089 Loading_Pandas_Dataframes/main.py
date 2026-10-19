import pandas as pd

df = pd.read_csv('exercises.csv', sep='\s*,\s*', index_col=0)

print(df)

print()

print(df.head())

print()

print(df.columns)