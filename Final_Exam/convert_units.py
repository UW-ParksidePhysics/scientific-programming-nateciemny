"""
Converts values between specified physical units using SciPy constants.
Supports volume, energy, and bulk modulus conversions for physics applications.
"""

__author__ = "Nate Ciemny"

from scipy.constants import physical_constants

def convert_units(value, units_from, units_to):
    """
    Converts a scalar value from one unit to another using known conversion factors.

    Parameters:
        value: numeric value to convert
        units_from: string describing original units
        units_to: string describing target units

    Returns:
        Converted value in new units

    Raises:
        ValueError: if the unit conversion is not supported
    """
    conversion_factors = {
        ('bohr^3', 'angstrom^3'): 0.14818471147216278,
        ('rydberg', 'electronvolt'): 13.605693122994,
        ('rydberg/bohr^3', 'gigapascal'): 14710.507848260711
    }

    key = (units_from, units_to)
    if key not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {units_from} to {units_to}")

    return value * conversion_factors[key]

if __name__ == "__main__":
    # Required test conversions
    volume_in_angstrom = convert_units(1, 'bohr^3', 'angstrom^3')
    print(f"1 bohr^3 = {volume_in_angstrom} angstrom^3")

    energy_in_electronvolt = convert_units(1, 'rydberg', 'electronvolt')
    print(f"1 rydberg = {energy_in_electronvolt} electronvolt")

    bulk_modulus_in_gigapascal = convert_units(1, 'rydberg/bohr^3', 'gigapascal')
    print(f"1 rydberg/bohr^3 = {bulk_modulus_in_gigapascal} gigapascal")
