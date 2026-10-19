import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=['Dogs', 'Cats', 'Mice'],
    index=['Meat', 'Fish', 'Vegetables'],
)

print(df)

print()

print(df['Cats'])

print()

cats = df['Cats']
print(cats.index)
print(list(cats.index))

print()

print(cats.values)
print("type of :", type(cats.values))