def powersOfTwo():
    for i in range(8):
        yield 2**i

for x in powersOfTwo():
    print(x)

print(type(powersOfTwo()))