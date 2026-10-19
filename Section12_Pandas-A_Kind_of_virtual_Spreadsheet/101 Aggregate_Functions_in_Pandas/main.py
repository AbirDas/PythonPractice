import pandas as pd

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

print(df.loc[:,"Age":"Spending"].mean())

print()

print(df['Age'])

print()

print(df['Age'].mean())

print()

gp = df.groupby("Gender")
print(gp.mean())
print()
print("Group for female:", gp.mean().loc["Female"])
print()
print("Group for male:", gp.mean().loc["Male"])
print()
print("Group for female only Age:", gp.mean().loc['Female','Age'])