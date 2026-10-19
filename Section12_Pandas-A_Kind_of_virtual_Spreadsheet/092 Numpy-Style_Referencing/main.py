import pandas as pd

df = pd.read_csv('exercises.csv', sep=',', index_col=0)
df.columns = df.columns.str.strip()
print(df)

print()

print(df.loc['Mon':'Wed'])

print()

print(df.loc['Mon':'Sun':2])

print()

print(df.loc[['Fri','Mon'], 'Pushups':'Squats'])

print()

print(df.loc[:,'Pushups':'Squats'])

print()

print(df.iloc[:,1:3])