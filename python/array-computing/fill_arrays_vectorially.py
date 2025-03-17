import numpy as np


def gaussian(position):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * position ** 2)


if __name__ == '__main__':
    # 41 values from -4 to 4
    x_values = np.linspace(-4, 4, 41)

    # Vectorized computation of y_values
    y_values = gaussian(x_values)

    # Print results
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.2f}, g(x) = {y:.5f}")
