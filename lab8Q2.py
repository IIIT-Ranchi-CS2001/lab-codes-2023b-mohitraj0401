import numpy as np

shape_A1 = tuple(map(int, input("Enter shape of A1 (rows, columns, depth): ").split()))
shape_A2 = tuple(map(int, input("Enter shape of A2 (rows, columns, depth): ").split()))

A1 = np.random.randint(1, 100, size=shape_A1)
A2 = np.random.randint(1, 100, size=shape_A2)

A1_div_5 = A1[A1 % 5 == 0]
A2_div_4 = A2[A2 % 4 == 0]

combined = np.concatenate((A1_div_5, A2_div_4))

side_length = int(np.floor(np.sqrt(len(combined))))
square_matrix = combined[:side_length**2].reshape(side_length, side_length)

print("Largest square matrix:", square_matrix)
