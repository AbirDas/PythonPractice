import pandas as pd

df = pd.read_csv('exercises.csv', sep=',', index_col=0)
df.columns = df.columns.str.strip()

print("Old Pushups value:",df.at['Tue','Pushups'])

df.at['Tue','Pushups'] = 40

print("Using iat to get Mon,Squarts:",df.iat[0,2])

print()

print(df)