"""
Reads in two-column numerical data from a text file.
Returns a NumPy array of shape (2, M) where M is the number of data points.
Raises OSError if the file cannot be found.
"""

__author__ = "Nate Ciemny"

import numpy as np
import os

def read_two_columns_text(filename):
    """
    Read in two columns of numerical data from text file

    Parameters:
        filename: name of file to be read

    Returns:
        2D array of shape containing x-y data
    """
    if not os.path.isfile(filename):
        raise OSError(f"The file '{filename}' was not found.")

    try:
        data_array = np.loadtxt(filename).T
        if data_array.shape[0] != 2:
            raise ValueError("Input file does not contain exactly two columns.")
        return data_array
    except Exception as exception:
        raise OSError(f"Error reading file '{filename}': {exception}")

if __name__ == "__main__":
    try:
        data = read_two_columns_text("Al.Fm-3m.GGA-PBE.volumes_energies.dat")
        print(f'{data=}, shape={data.shape}')
    except OSError as error:
        print(error)


