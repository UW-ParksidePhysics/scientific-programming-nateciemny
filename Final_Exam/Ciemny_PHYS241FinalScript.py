"""
Final project script for PHYS241 — Equation of State and Quantum Analysis.

   Fits a Murnaghan equation of state to DFT energy–volume data, and:
   - Extracts metadata from the file name.
   - Normalizes data per atom based on crystal symmetry.
   - Fits a quadratic curve for initial parameters.
   - Uses least-squares fitting and unit conversion.
   - Generates a labeled plot of the EOS fit and saves it.
   Solves the 1D Schrödinger equation for a harmonic potential:
   - Constructs the Hamiltonian matrix.
   - Extracts the lowest eigenvectors and eigenvalues.
   - Plots selected wave functions on a spatial grid.
   - Annotates and saves the plot.
All major functionality is imported from external modules. The script is
designed to be run directly and controlled via the `display_graph` flag.
"""

__author__ = "Nate Ciemny"

import numpy as np
import matplotlib.pyplot as plt
import datetime
from read_two_columns_text import read_two_columns_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from equations_of_state import fit_equation_of_state
from convert_units import convert_units
from annotate_plot import annotate_plot
from generate_matrix import generate_matrix
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors

def parse_file_name(file_name):
    """
    Extracts data from a file name
    Parameters:
        file_name (str): Full name of the file in the format
                         Chemical.Crystal.DFT.volumes_energies.dat
    Returns:
        tuple: (chemical_symbol, crystal_symmetry_symbol,
                density_functional_approximation)
    """
    name_components = file_name.split("/")[-1].split(".")
    chemical_symbol = name_components[0]
    crystal_symmetry_symbol = name_components[1]
    density_functional_approximation = name_components[2]
    return chemical_symbol, crystal_symmetry_symbol, density_functional_approximation

if __name__ == "__main__":
    display_graph = True
    file_name = "Al.Fm-3m.GGA-PBE.volumes_energies.dat"
    chemical_symbol, crystal_symmetry_symbol, density_functional_approximation = parse_file_name(file_name)
    data_array = read_two_columns_text(file_name)

    if crystal_symmetry_symbol == "Fm-3m":
        number_of_atoms_per_cell = 1
    elif crystal_symmetry_symbol == "Fd-3m":
        number_of_atoms_per_cell = 2
    else:
        raise ValueError("Unknown crystal symmetry symbol. Please specify atom count manually.")

    volume_array_per_atom = data_array[0] / number_of_atoms_per_cell
    energy_array_per_atom = data_array[1] / number_of_atoms_per_cell
    adjusted_data_array = np.vstack((volume_array_per_atom, energy_array_per_atom))
    statistical_summary = calculate_bivariate_statistics(adjusted_data_array)
    quadratic_coefficients = calculate_quadratic_fit(adjusted_data_array)

    equation_of_state_curve, equation_of_state_parameters = fit_equation_of_state(
        volume_array_per_atom,
        energy_array_per_atom,
        quadratic_coefficients,
        equation_of_state="Murnaghan",
        number_of_points=50
    )
    equation_of_state_volume_grid = np.linspace(
        np.amin(volume_array_per_atom),
        np.amax(volume_array_per_atom),
        50  # same number_of_points used in EOS fit
    )
    equation_of_state_volume_grid_angstrom = convert_units(
        equation_of_state_volume_grid,
        "bohr^3",
        "angstrom^3"
    )
    equation_of_state_energy_curve_electronvolt = convert_units(
        equation_of_state_curve,
        "rydberg",
        "electronvolt"
    )
    bulk_modulus_rydberg_per_bohr3 = equation_of_state_parameters[1]
    bulk_modulus_gigapascal = convert_units(
        bulk_modulus_rydberg_per_bohr3,
        "rydberg/bohr^3",
        "gigapascal"
    )

    figure, axis = plt.subplots()
    axis.plot(
        equation_of_state_volume_grid_angstrom,
        equation_of_state_energy_curve_electronvolt,
        color="black",
        linestyle="-",
        linewidth=2,
        label="Equation of State Fit"
    )
    volume_data_angstrom = convert_units(volume_array_per_atom, "bohr^3", "angstrom^3")
    energy_data_electronvolt = convert_units(energy_array_per_atom, "rydberg", "electronvolt")
    equation_of_state_energy_curve_electronvolt = convert_units(equation_of_state_curve, "rydberg", "electronvolt")
    axis.plot(
        volume_data_angstrom,
        energy_data_electronvolt,
        linestyle="None",
        marker="o",
        markersize=6,
        color="blue",
        label="DFT Data Points"
    )

    volume_min = min(volume_data_angstrom)
    volume_max = max(volume_data_angstrom)
    energy_min = min(energy_data_electronvolt)
    energy_max = max(energy_data_electronvolt)
    volume_range = volume_max - volume_min
    energy_range = energy_max - energy_min

    axis.set_xlim(volume_min - 0.1 * volume_range, volume_max + 0.1 * volume_range)
    axis.set_ylim(energy_min - 0.1 * energy_range, energy_max + 0.1 * energy_range)
    axis.set_xlabel(r"$V$ ($\mathrm{\AA}^3$/atom)")
    axis.set_ylabel(r"$E$ (eV/atom)")
    axis.legend()

    equilibrium_volume = equation_of_state_parameters[3]
    equilibrium_volume_angstrom = convert_units(equilibrium_volume, "bohr^3", "angstrom^3")
    today_date_string = datetime.date.today().isoformat()
    formatted_crystal_symmetry_symbol = r"$\it{Fm\overline{3}m}$"
    annotations = {
        chemical_symbol: {
            'position': (volume_min - 0.06 * volume_range, energy_max + 0.03 * energy_range),
            'alignment': ['left', 'bottom'],
            'fontsize': 10
        },
        formatted_crystal_symmetry_symbol: {
            'position': ((volume_min + volume_max) / 2, energy_max - 0.56 * energy_range),
            'alignment': ['center', 'bottom'],
            'fontsize': 10
        },
        r"$K_0 = $" + f"{bulk_modulus_gigapascal:.1f} GPa": {
            'position': ((volume_min + volume_max) / 2, energy_max - 0.5 * energy_range),
            'alignment': ['center', 'bottom'],
            'fontsize': 10
        },
        f"$V_0 = {equilibrium_volume_angstrom:.2f}$ $\\mathrm{{\\AA^3}}$/atom": {
            'position': (equilibrium_volume_angstrom + 0.16 * volume_range, energy_min - 0.01 * energy_range),
            'alignment': ['center', 'top'],
            'fontsize': 10
        },
        f"Created by Nate Ciemny {today_date_string}": {
            'position': (volume_min - 0.35 * volume_range, energy_min - 0.25 * energy_range),
            'alignment': ['left', 'top'],
            'fontsize': 8
        }
    }
    eos_energy_minimum = np.min(equation_of_state_energy_curve_electronvolt)
    line_top = (eos_energy_minimum + energy_min) / 1
    axis.vlines(
        x=equilibrium_volume_angstrom,
        ymin=energy_min,
        ymax=line_top,
        color="black",
        linestyle="--",
        linewidth=1
    )
    axis.set_title(f"Murnaghan Equation of State for {chemical_symbol} in DFT ({density_functional_approximation})", pad = 20)

    annotate_plot(annotations)
    plt.tight_layout()
    plt.draw()
    figure.subplots_adjust(left=0.18)
    axis.tick_params(axis='y', labelsize=10)
    plot_file_name = f"Ciemny.{chemical_symbol}.{crystal_symmetry_symbol}.{density_functional_approximation}.MurnaghanEquationOfState.png"

    if display_graph:
        plt.show()
    else:
        plt.savefig(plot_file_name, dpi=300, bbox_inches="tight")
        plt.close()
### PART 2 ###
    number_of_dimensions = 120
    spatial_domain = [-2.0, 2.0]
    potential_name = "harmonic"
    potential_parameter = 1.0

    hamiltonian_matrix = generate_matrix(
        minimum_x=spatial_domain[0],
        maximum_x=spatial_domain[1],
        number_of_dimensions=number_of_dimensions,
        potential_name=potential_name,
        potential_parameter=potential_parameter
    )
    eigenvector_indices = [1, 2, 3]
    eigenvalue_array, eigenvector_array = calculate_lowest_eigenvectors(
        hamiltonian_matrix,
        number_of_eigenvectors=max(eigenvector_indices) + 1
    )
    eigenvector_array = eigenvector_array.T

    spatial_grid = np.linspace(-10.0, 10.0, number_of_dimensions)
    figure, axis = plt.subplots()
    color_cycle = ['blue', 'green', 'red']
    max_component_value = 0

    for i, eigenvector_index in enumerate(eigenvector_indices):
        eigenvector = eigenvector_array[:, eigenvector_index]
        eigenvalue = eigenvalue_array[eigenvector_index]

        if eigenvector_index == 0 and np.sum(eigenvector) < 0:
            eigenvector *= -1
        max_component_value = max(max_component_value, np.max(np.abs(eigenvector)))

        label = rf"$\psi_{{{eigenvector_index}}},\ E_{{{eigenvector_index}}} = {eigenvalue:.4f}\ \mathrm{{a.u.}}$"
        axis.plot(spatial_grid, eigenvector, linewidth=2, color=color_cycle[i], label=label)
    axis.set_xlabel(r"$x$ [a.u.]")
    axis.set_ylabel(r"$\psi_n(x)$ [a.u.]")
    axis.set_ylim(-2 * max_component_value, 2 * max_component_value)
    axis.axhline(
        y=0.0,
        color="black",
        linestyle="-",
        linewidth=1
    )
    axis.legend()

    today_date_string = datetime.date.today().isoformat()
    annotations = {
        f"Created by Nate Ciemny {today_date_string}": {
            'position': (spatial_grid[0] - 3.5, -2.6 * max_component_value),
            'alignment': ['left', 'top'],
            'fontsize': 8
        }
    }
    annotate_plot(annotations)

    eigenvector_plot_filename = "Ciemny.Harmonic.Eigenvector123.png"
    axis.set_title(
        f"Select Wave Functions for a {potential_name.capitalize()} Potential on a Spatial Grid of {number_of_dimensions} Points",
        pad=20)
    plt.tight_layout()

    if display_graph:
        plt.show()
    else:
        plt.savefig(eigenvector_plot_filename, dpi=300, bbox_inches="tight")
        plt.close()