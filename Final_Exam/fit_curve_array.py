"""
Create a fit curve using polynomial coefficients and an x-range.
Returns a 2-row array of x and y values evaluated from the polynomial.
"""

__author__ = "Nate Ciemny"

import numpy as np

def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points=100):
    """
    Create fit curve from quadratic coefficients and x-limits

    Parameters:
        quadratic_coefficients: list or array of length 3
        minimum_x: starting x-value for fit curve
        maximum_x: ending x-value for fit curve
        number_of_points: number of points in the output curve

    Returns:
        2-row array of x and y values: shape

    Raises:
        ArithmeticError: if maximum_x < minimum_x
        IndexError: if number_of_points <= 2
    """
    if maximum_x < minimum_x:
        raise ArithmeticError("Ending x-value must be greater than or equal to starting x-value.")
    if number_of_points <= 2:
        raise IndexError("Number of points must be greater than 2.")

    x_values = np.linspace(minimum_x, maximum_x, number_of_points)

    # Coefficients were given in [constant, linear, quadratic], so reverse for numpy.polyval
    y_values = np.polyval(quadratic_coefficients[::-1], x_values)

    return np.vstack((x_values, y_values))

if __name__ == "__main__":
    coefficients = [0, 0, 1]  # y = x^2
    fit_curve = fit_curve_array(coefficients, -2, 2, number_of_points=5)
    print(f'{fit_curve=}, shape={fit_curve.shape}')
