import numpy as np
import matplotlib.pyplot as plt

def vertical_trajectory(initial_velocity, gravitational_acceleration, time):
    return (initial_velocity * time) - (.5 * gravitational_acceleration * time * time)



if __name__ == '__main__':
    print(vertical_trajectory(2, 9.8, 0))