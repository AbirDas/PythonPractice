import numpy as np

values = np.arange(16).reshape(4, 4)
print(values)

print()

print(values[1:4:2,:])

print()

print(values[[0, 2]])

print()

print(values[:,[0,2]])

print()
#picking 0 & 8 & 10 & 13 specific value

print(values[[0,2,2,3],[0,0,2,1]])
