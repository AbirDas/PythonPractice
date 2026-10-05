fruits = ["apple", "orange", "grape"]

print(id(fruits))
fruits += ["melon"]
print(id(fruits))
print(fruits)

print()

fruits[0] = "strawberry"
print(id(fruits))
print(fruits)

fruits.append("pear")
print(fruits)

topicalFruits = ["guava","jackfruit"]
fruits.extend(topicalFruits)
print(fruits)

fruits.insert(2, "kiwi")
print(fruits)
print()

fruits_tuple = tuple(fruits)
print(fruits_tuple)
fruits_list = list(fruits_tuple)
print(fruits_list)