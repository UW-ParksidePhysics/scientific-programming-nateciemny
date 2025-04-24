import math

def gaussian(position):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position ** 2)

if __name__ == '__main__':
    # Parameters
    start = -4
    end = 4
    num_points = 41
    step = (end - start) / (num_points - 1)

    # Arrays
    x_values = []
    y_values = []

    # Fill arrays using a for loop
    for i in range(num_points):
        x = start + i * step
        y = gaussian(x)
        x_values.append(x)
        y_values.append(y)

    # Print results
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.2f}, g(x) = {y:.5f}")
