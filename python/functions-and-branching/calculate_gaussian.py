import math

def gaussian(position, mean=0, standard_deviation=1):
    """Computes the Gaussian function value for a given x (position)."""
    coefficient = 1 / (math.sqrt(2 * math.pi) * standard_deviation)
    exponent = math.exp(-0.5 * ((position - mean) / standard_deviation) ** 2)
    return coefficient * exponent

if __name__ == '__main__':
    # Define mean, standard deviation, and number of points
    mean = 0
    sigma = 1
    n = 11  # Number of points

    # Calculate n uniformly spaced x values in range [mean - 5σ, mean + 5σ]
    x_values = [mean - 5 * sigma + i * (10 * sigma / (n - 1)) for i in range(n)]

    # Compute Gaussian values
    f_values = [gaussian(x, mean, sigma) for x in x_values]

    # Print table
    print(f"{'x':^10} {'f(x)':^15}")
    print("="*26)
    for x, f in zip(x_values, f_values):
        print(f"{x:^10.3f} {f:^15.6f}")