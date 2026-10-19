import pandas as pd

data = {
    "Mon" : [1,2,3],
    "Tue" : [0.2,0.3,0.4],
    "Wed" : [7,8,9]
}

df = pd.DataFrame(data)

print(df)