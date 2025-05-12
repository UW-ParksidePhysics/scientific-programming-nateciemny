"""
Identify eigenvectors corresponding to the smallest eigenvalues of a square matrix.
Returns eigenvalues and eigenvectors sorted by increasing eigenvalue.
"""

__author__ = "Nate Ciemny"

import numpy

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    """
    Calculate eigenvectors corresponding to the smallest eigenvalues of a square matrix

    Parameters:
        square_matrix: 2D square array
        number_of_eigenvectors: number of lowest eigenvalues to return

    Returns:
        eigenvalues: 1D array of K smallest eigenvalues, sorted
        eigenvectors: 2D array of shape, each row is an eigenvector
    """
    if square_matrix.shape[0] != square_matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    eigenvalues, eigenvectors = numpy.linalg.eig(square_matrix)

    # Sort eigenvalues
    sorted_indices = numpy.argsort(eigenvalues)
    selected_indices = sorted_indices[:number_of_eigenvectors]

    lowest_eigenvalues = eigenvalues[selected_indices]
    lowest_eigenvectors = eigenvectors[:, selected_indices].T

    return lowest_eigenvalues, lowest_eigenvectors

if __name__ == "__main__":
    test_matrix = numpy.array([[2, -1], [-1, 2]])
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(test_matrix, number_of_eigenvectors=2)

    print(f'{eigenvalues=}')
    print(f'{eigenvectors=}')
