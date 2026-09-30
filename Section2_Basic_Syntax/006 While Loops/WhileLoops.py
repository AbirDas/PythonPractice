value = 0

while value < 5:
    value += 1

    if value == 2:
        continue

    print("while",value)
else:
    print("Finished")