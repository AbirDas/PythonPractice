letters = [chr(x) for x in range(65,91)]
print(letters)

print()

lowerletters = (chr(x) for x in range(97,123))
print(lowerletters)
#print(list(lowerletters))
#print(list(lowerletters))

for i in lowerletters:
    print(i, end=" ")