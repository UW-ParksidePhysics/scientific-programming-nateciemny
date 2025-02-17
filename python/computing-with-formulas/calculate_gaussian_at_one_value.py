import math

# Define variables
mean = 0
standard_deviation = 2
input_value = 1

# Calculate the Gaussian function
gaussian_value = (1 / (math.sqrt(2 * math.pi) * standard_deviation)) * math.exp(-0.5 * ((input_value - mean) / standard_deviation) ** 2)

# Print inputs and output
print(f"Mean (m): {mean}")
print(f"Standard Deviation (s): {standard_deviation}")
print(f"Input Value (x): {input_value}")
print(f"Gaussian Function Value: {gaussian_value}")