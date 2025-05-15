"""
Create a combined plot of original data and polynomial fit using Pyplot.
Returns the list of plot objects created.
"""

__author__ = "Nate Ciemny"

import numpy as np
import matplotlib.pyplot as pyplot

def plot_data_with_fit(data, fit_curve, data_format='o', fit_format=''):
    """
    Create a combined scatter and curve plot for x-y data and its fit curve

    Parameters:
        data: 2-row array of x-y values
        fit_curve: 2-row array of x-y values, from fitted polynomial
        data_format: optional format string for data points
        fit_format: optional format string for fit curve

    Returns:
        List of Line2D plot objects
    """
    data_plot = pyplot.plot(data[0], data[1], data_format)
    fit_plot = pyplot.plot(fit_curve[0], fit_curve[1], fit_format)
    return data_plot + fit_plot

if __name__ == "__main__":
    data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
    x_values = np.linspace(-2, 2, 100)
    y_values = x_values ** 2
    fit_curve = np.vstack((x_values, y_values))

    combined_plot = plot_data_with_fit(data, fit_curve, data_format='x', fit_format='--')
    pyplot.show()
