import numpy as np

values1 = np.random.rand(2, 3)
print(values1)

print()

rng = np.random.default_rng()
values2 = rng.standard_normal(10)
print(values2)

print()

values3 = rng.standard_normal((4,3))
print(values3)

print()

print(values3.reshape(2, 6))