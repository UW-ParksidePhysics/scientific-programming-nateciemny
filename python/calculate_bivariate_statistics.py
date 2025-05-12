"""
Calculate statistical characteristics of a 2-row data set using SciPy's stats.describe.
Returns six values describing the x and y columns.
Raises IndexError if the array does not have two rows or has fewer than two data points.
"""

__author__ = "Nate Ciemny"

import numpy
from scipy import stats

def calculate_bivariate_statistics(data):
    """
    Calculate statistical characteristics of a 2-row x-y dataset.

    Parameters:
        data: x-y data array of shape (2, M)

    Returns:
        Array of shape (6,) containing:
        [mean of y, standard deviation of y, min x, max x, min y, max y]
    """
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError("Input data must have shape (2, M) where M > 1.")

    x_values = data[0]
    y_values = data[1]

    description = stats.describe(y_values)

    mean_y = description.mean
    std_dev_y = numpy.sqrt(description.variance)
    min_x = numpy.min(x_values)
    max_x = numpy.max(x_values)
    min_y = description.minmax[0]
    max_y = description.minmax[1]

    return numpy.array([mean_y, std_dev_y, min_x, max_x, min_y, max_y])

if __name__ == "__main__":
    x_values = numpy.linspace(-10, 10, 100)
    y_values = x_values ** 2
    test_data = numpy.vstack((x_values, y_values))

    statistics = calculate_bivariate_statistics(test_data)
    print(f'{statistics=}, shape={statistics.shape}')


