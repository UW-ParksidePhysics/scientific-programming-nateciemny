import math

# Define constants
rho = 1.038  # Density of egg (g/cm^3)
c = 3.7     # Specific heat capacity (J/g K)
k = 5.4e-3  # Thermal conductivity (W/(cm K))
Tw = 100    # Boiling water temperature (°C)
Ty = 70     # Desired yolk temperature (°C)

# Masses of eggs
small_egg_mass = 47  # Small egg mass (g)
large_egg_mass = 67  # Large egg mass (g)

# Initial temperatures
T0_fridge = 4   # Egg temperature from fridge (°C)
T0_room = 20    # Egg temperature from room (°C)

# Function to calculate cooking time
def calculate_cook_time(mass, T0):
    # Calculate time using the given formula
    t = (mass ** (2/3) * c * rho ** (1/3)) / (k * (math.pi * 4 / 3) ** (2/3)) * \
        math.log(0.76 * (T0 - Tw) / (Ty - Tw))
    return t / 60  # Convert seconds to minutes

# Calculate times for each condition
times = {
    "Small Egg from Fridge": calculate_cook_time(small_egg_mass, T0_fridge),
    "Small Egg from Room": calculate_cook_time(small_egg_mass, T0_room),
    "Large Egg from Fridge": calculate_cook_time(large_egg_mass, T0_fridge),
    "Large Egg from Room": calculate_cook_time(large_egg_mass, T0_room)
}

# Print results
print("Egg Cooking Times (in minutes):")
for condition, time in times.items():
    print(f"{condition}: {time:.1f} minutes")