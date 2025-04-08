import numpy as np
import matplotlib.pyplot as plt




def vertical_trajectory(initial_velocity, gravitational_acceleration, time):
    return (initial_velocity * time) - (.5 * gravitational_acceleration * time * time)

starting_velocity = 2 #m/s
gravitational_acceleration = 9.8 #m/s/s

if __name__ == '__main__':
    times = np.linspace(0, 5)
    trajectories = vertical_trajectory(times, starting_velocity, gravitational_acceleration)
    print(vertical_trajectory(2, 9.8, 5))
    plt.plot(times, vertical_trajectory(2, 9.8, 5))
    plt.show()
