"""
This code takes the distances between each planet and creates an icon representing each planet.

https://github.com/williamdparker/AstronomyCalculations/blob/master/solar_system_sign_icons/draw_logarithmic_distance_ruler.py
Black and white and color version. Overlay image of planet of interest. Label unit of the ruler (astronomical unit). Give conversion
in miles and kilometers. Make 1.5 in. version and 3.5 in. version.
https://github.com/williamdparker/AstronomyCalculations/tree/master/solar_system_sign_icons



"""
__author__ = "Nate Ciemny"

import numpy as np
import matplotlib.pyplot as plt

from python.vpython.two_balls_bounce import initial_velocity


def velocity_in_time(time, initial_velocity=0, gravitational_acceleration=9.8):
    return initial_velocity - gravitational_acceleration * time

def test_plot():


    intercepts = [4, 3]
    x_bounds = np.array([-3, 8])
    x_values = np.linspace(x_bounds[0], x_bounds[1], 100)
    # y_bounds = -intercepts[1] * x_bounds / intercepts[0] + intercepts[1]
    y_values = -intercepts[1] * x_values / intercepts[0] + intercepts[1]

    # circle
    radius = intercepts[0]
    angles = np.linspace(0, 2 * np.pi, 100)
    circle_xs = radius * np.cos(angles)
    circle_ys = radius * np.sin(angles)

    # plt.plot(x_bounds, y_bounds)
    plt.plot(x_values, y_values)
    plt.plot(circle_xs, circle_ys)
    plt.show()

    return

if __name__ == '__main__':
    object_data = {'Earth': 9.8, 'Moon': 1.6, 'Mars': 3.7} # surface gravity [m/s/s]
    starting_velocity = 10 # m/s
    times = np.linspace(0, 5)
    for planet_data in object_data.items():
        velocities = velocity_in_time(times, initial_velocity=starting_velocity, gravitational_acceleration=planet_data[1])
        plt.plot(times, velocities, label=planet_data[0])

        plt.text(0, velocities[-1], f'Initial velocity: {starting_velocity:.0f} m/s')
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.legend()
        plt.show()

# test_plot()

#### RENAME from planet_distance.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization
