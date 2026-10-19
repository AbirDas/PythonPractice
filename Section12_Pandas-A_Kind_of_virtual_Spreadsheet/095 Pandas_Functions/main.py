import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=['Dogs', 'Cats', 'Mice'],
    index=['Meat', 'Fish', 'Vegetables'],
)

print(df)

print()

print(df.sum())
print("Type of df:",type(df))
print("Type of df sum:",type(df.sum()))