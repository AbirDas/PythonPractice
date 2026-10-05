numbers = [0, 1, 2, 3, 4, 5, 6]

print(numbers)
numbers.remove(4)
print(numbers)

print()

numbers.pop()
print(numbers)
value = numbers.pop(1)
print(value,numbers)

del numbers[2]
print(numbers)

numbers.clear()
print(numbers)