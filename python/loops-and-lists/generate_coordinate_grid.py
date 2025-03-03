# Define interval and number of intervals
a = 1  # Start of interval
b = 2  # End of interval
num_intervals = 20  # Number of intervals

# Calculate interval length h
h = (b - a) / num_intervals

# For loop for coordinates
coordinates_for_loop = []
for i in range(num_intervals + 1):  # Including the endpoint
    coordinates_for_loop.append(round(a + i * h, 2))  # Rounding to match expected output format

# List comprehension for coordinates
coordinates_list_comprehension = [round(a + i * h, 2) for i in range(num_intervals + 1)]

# Print results
print(f"For x in [{a}, {b}] with {num_intervals} intervals, the interval length is h = {h:.3f}, and")
print("Using a for loop:")
print(f"x = {coordinates_for_loop}")
print("Using list comprehension:")
print(f"x = {coordinates_list_comprehension}")