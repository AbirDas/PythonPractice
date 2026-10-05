stuff = ("Abir", 38, 5.7, True, False, "Cats")

print(stuff[2])
#can't change the list ideam tuples containers is imutable, can not do below
#stuff[2] = "kumar"

print()

name, age, height, bool1, bool2, animal = stuff
print(name, age, height, bool1, bool2, animal)

print()

person, number1, number2, *others = stuff
print(person, number1, number2, others)
print(type(others))

print()

animals = ("cat",)
print(animals)
print(type(animals))