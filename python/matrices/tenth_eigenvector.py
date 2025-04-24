import numpy as np
import matplotlib.pyplot as plt

matrix_dimension = 10
grid_spacing = 1 / ( matrix_dimension+ 1)

main_diag = 2 * np.ones(matrix_dimension)
off_diag = -1 * np.ones(matrix_dimension - 1)

matrix = (
    np.diag(main_diag) +
    np.diag(off_diag, k=1) +
    np.diag(off_diag, k=-1)
) / (2 * grid_spacing**2)

eigenvalues, eigenvectors = np.linalg.eig(matrix)
index = np.argsort(eigenvalues)[-1]
fifth_vector = eigenvectors[:, index]

x_coordinate = np.linspace(1 / (matrix_dimension + 1), matrix_dimension / (matrix_dimension + 1), matrix_dimension)
reference = np.sqrt(2) * np.sin(np.pi * x_coordinate)

plt.plot(x_coordinate, fifth_vector, 'o-', label='5th Eigenvector')
plt.plot(x_coordinate, reference, 'r--', label=r'$\sqrt{2} \sin(\pi x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Comparison with $\sqrt{2} \sin(\pi x)$')
plt.show()
