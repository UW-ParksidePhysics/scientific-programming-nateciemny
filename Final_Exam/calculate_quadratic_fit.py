"""
Fit a quadratic polynomial to x-y data using NumPy's polyfit method.
Returns polynomial coefficients in the order: constant, linear, quadratic.
"""

__author__ = "Nate Ciemny"

import numpy as np

def calculate_quadratic_fit(data):
    """
    Fit quadratic polynomial to a two-row x-y dataset

    Parameters:
        data: x-y data array of shape

    Returns:
        Array of shape with polynomial coefficients:
        [constant_term, linear_term, quadratic_term]
    """
    if data.ndim != 2 or data.shape[0] != 2:
        raise IndexError("Input data must have shape (2, M) for x-y values.")

    x_values = data[0]
    y_values = data[1]

    coefficients = np.polyfit(x_values, y_values, 2)
    return coefficients[::-1]

if __name__ == "__main__":
    x_values = np.linspace(-1, 1, 11)
    y_values = x_values ** 2
    test_data = np.vstack((x_values, y_values))

    quadratic_coefficients = calculate_quadratic_fit(test_data)
    print(f'{quadratic_coefficients=}, shape={quadratic_coefficients.shape}')


