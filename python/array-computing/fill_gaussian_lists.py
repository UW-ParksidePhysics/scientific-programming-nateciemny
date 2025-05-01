import math

def gaussian(position):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position ** 2)

if __name__ == '__main__':
    # Generate 41 uniformly spaced values between -4 and 4
    start = -4
    end = 4
    num_points = 41
    step = (end - start) / (num_points - 1)

    positions = [start + i * step for i in range(num_points)]
    gaussian_values = [gaussian(x) for x in positions]

    # Print values
    for pos, val in zip(positions, gaussian_values):
        print(f"x = {pos:.2f}, g(x) = {val:.5f}")