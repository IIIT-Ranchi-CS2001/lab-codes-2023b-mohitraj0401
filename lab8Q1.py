import numpy as np

A = np.array([
    [44, 38, 21],
    [32, 28, 15],
    [24, 20, 10]
])

B = np.array([1412, 1024, 728])

X = np.linalg.solve(A, B)

print("Number of males, females, and kids:", X)
