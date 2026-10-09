numbers = list((0,1,2,3,4,5,6,7))

print(numbers)
print(id(numbers))
numbers[2:4] = (0,0,0,0)
print(id(numbers))
print(numbers)

print()

print(numbers[2:6])
numbers[2:6] = []
print(numbers)

print()

numbers[1::2] = ["hello", "to", "you"]
print(numbers)