import numpy as np
import matplotlib.pyplot as plt


def gaussian(position):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * position ** 2)


if __name__ == '__main__':
    # Generate x values
    x_values = np.linspace(-4, 4, 1000)

    # Compute Gaussian values
    y_values = gaussian(x_values)

    # Plot values
    plt.plot(x_values, y_values, label='g(x)', color='blue')
    plt.title('Gaussian Function $g(x) = \\frac{1}{\\sqrt{2\\pi}} e^{-\\frac{1}{2}x^2}$')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.grid(True)
    plt.legend()
    plt.show()