with open("test.txt") as file:
    #lines = file.readlines()
    #print(lines)

    #print()

    newLines = file.read().splitlines()
    print(newLines)

    #need to implement below to auto open and close file like try block in java
    # __enter__
    # __exit__