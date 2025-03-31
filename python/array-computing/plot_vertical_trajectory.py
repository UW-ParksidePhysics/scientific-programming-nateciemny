import sys
import numpy as np
import matplotlib.pyplot as plt

def y(t, v0, g):
    return v0 * t - 0.5 * g * t**2

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <g> <v0_1> <v0_2> ... <v0_n>")
        sys.exit(1)

    g = float(sys.argv[1])
    initial_velocities = [float(v) for v in sys.argv[2:]]

    for v0 in initial_velocities:
        t_max = 2 * v0 / g
        t_values = np.linspace(0, t_max, 100)
        y_values = y(t_values, v0, g)
        plt.plot(t_values, y_values, label=f'v0 = {v0}')

    plt.title('Projectile Motion Curves')
    plt.xlabel('Time (t)')
    plt.ylabel('Height (y)')
    plt.legend()
    plt.grid(True)
    plt.show()
