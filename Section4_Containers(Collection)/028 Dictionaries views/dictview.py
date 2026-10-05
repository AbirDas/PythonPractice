people = {
    "Bob" : 42,
    "Sue" : 53,
    "Steve" :  25,
}

print(people)

print()

keys = people.keys()
values = people.values()
items = people.items()

print(type(keys))
print(type(values))
print(type(items))

print()

item_list = list(items)
print(item_list)

print(items)
del people["Sue"]
print(items)

print(item_list)

item_list = list(items)
print(item_list)