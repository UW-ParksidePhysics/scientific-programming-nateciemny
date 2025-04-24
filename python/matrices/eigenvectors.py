import numpy as np


# matrix_three = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
# print(f'A_3 = \n{matrix_three}\n' )

size = 2
identity_matrix = np.identity(size)
negative_ones = np.full(size-1, -1)
down_shifted_negative_ones = np.diag(negative_ones, -1)
up_shifted_negative_ones = np.diag(negative_ones, 1)
combined_matrix = 2*identity_matrix + down_shifted_negative_ones + up_shifted_negative_ones
print(f'\n{combined_matrix}\n')

eigenvalues, eigenvectors = np.linalg.eig(combined_matrix)

for eigenvalues, eigenvectors in zip(eigenvalues, eigenvectors.transpose()):
    print(f'lambda = {eigenvalues}, x-vector = {eigenvectors}\n')