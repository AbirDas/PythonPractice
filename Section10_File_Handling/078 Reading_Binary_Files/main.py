with open('test1.bin', 'rb') as file:
    data = file.read(5)
    print(data)

with open('test2.bin', 'rb') as file:
    data = file.read(5)
    print(data)

print()

print(data[0])
print(data[1])

print()

print(len(data))