fruits = ("apple", "pear", "orange")
days = ("monday", "tuesday", "wednesday")

for i,fruit in enumerate(fruits):
    print(i,fruit)

print()

for fruit, day in zip(fruits,days):
    print(fruit,day)