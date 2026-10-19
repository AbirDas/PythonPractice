import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(0, 4, 60).reshape(20, 3),
    columns=['One', 'Two', 'Three'],
    index=[chr(x) for x in range(65, 85)]
    )
print(df)

print()

df1 = df.sort_values(by='One')
print(df1)

print()

df2 = df.sort_values(by=['One','Two','Three'])
print(df2)

print()

df3 = df.sort_values(by=['One', 'Two', 'Three'], ascending=False)
print(df3)

print()

df4 = df.transpose()
print(df4)
df4 = df4.sort_values(by=['One', 'Two', 'Three'], axis=1, ascending=False)
print(df4)