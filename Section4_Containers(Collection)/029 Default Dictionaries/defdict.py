from collections import defaultdict

people = {
    "Bob" : 42,
    "Sue" : 53,
    "Steve" : 25,
}

print(people["Bob"])
print(people.get("Sue"))

print()

#get can help in retriving if some value not present and give default value you passed.
print(people.get("Ethel"))
print(people.get("Ethel",99))


print()
print("Default Dict")
print()

days = defaultdict(str)

days.update({"Mon":"Monday", "Tue":"Tuesday"})

print(days)
print(days["Mon"])
print(days["Wed"])
