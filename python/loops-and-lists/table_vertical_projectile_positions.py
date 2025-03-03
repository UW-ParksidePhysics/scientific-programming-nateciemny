# Initial velocity
v0 = 10  # m/s

# Gravity values for two different objects
g1 = 14.12  # Gliese 667 Cb # m/s^2
g2 = 12.94  # Gliese 667 Cc # m/s^2

# Time
t_initial = 0
t_final1 = 2 * v0 / g1  # Time when object 1 hits the ground
t_final2 = 2 * v0 / g2  # Time when object 2 hits the ground
num_intervals = 8  # Number of intervals
dt1 = t_final1 / num_intervals
dt2 = t_final2 / num_intervals

# Print table header
print(f"For initial velocity of {v0:.2f} m/s:")
print("-" * 45)
print(f"{'Object 1 (g = 14.12 m/s²)':<20}{'Object 2 (g = 12.94 m/s²)'}")
print("-" * 45)
print(f"{'t (s)':<10}{'y (m)':<10}{'t (s)':<10}{'y (m)'}")
print(f"{'-'*10}{'-'*10}{'-'*10}{'-'*10}")

# For loop
print("Using a for loop:")
for i in range(num_intervals + 1):
    t1 = i * dt1
    t2 = i * dt2
    y1 = v0 * t1 - 0.5 * g1 * t1**2
    y2 = v0 * t2 - 0.5 * g2 * t2**2
    print(f"{t1:<10.3f}{y1:<10.3f}{t2:<10.3f}{y2:<10.3f}")

# While loop
print("Using a while loop:")
t1, t2 = t_initial, t_initial
while t1 <= t_final1 or t2 <= t_final2:

    if t1 <= t_final1:
        y1 = v0 * t1 - 0.5 * g1 * t1**2
        print(f"{t1:<10.3f}{y1:<10.3f}", end="")
        t1 += dt1
    else:
        print(" " * 20, end="")

    # Print
    if t2 <= t_final2:
        y2 = v0 * t2 - 0.5 * g2 * t2**2
        print(f"{t2:<10.3f}{y2:<10.3f}")
        t2 += dt2  # Increment time for object 2
    else:
        print()  # New line for spacing

print("-" * 45)