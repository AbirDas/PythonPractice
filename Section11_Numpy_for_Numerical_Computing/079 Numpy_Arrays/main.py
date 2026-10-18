import numpy as np

values1 = np.array([1, 2, 3], dtype=np.int32)

print(values1)
print(type(values1))
print(values1[1])

print()

print(values1.shape)
print(values1.ndim)
print(values1.dtype)
print(len(values1))

print()

values2 = np.array([[1.0, 2.1], [2.0, 3.1], [3.0, 4.1]], dtype=np.float64)

print(values2[1])
print(values2.shape)
print(values2.ndim)
print(values2.dtype)
print(len(values2))