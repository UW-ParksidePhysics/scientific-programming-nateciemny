# Initial condition
initial_velocity = 10.00  # m/s
g1 = 14.12  # m/s^2
g2 = 12.94  # m/s^2
t_final1 = 1.416  # s
t_final2 = 1.545  # s
dt1 = 0.177  # s
dt2 = 0.193  # s

# Lists
times1 = []
positions1 = []
times2 = []
positions2 = []

# Generate time and positions for object 1
t1 = 0
y1 = 0
while t1 <= t_final1:
    times1.append(t1)
    positions1.append(y1)
    t1 += dt1
    y1 = initial_velocity * t1 - 0.5 * g1 * t1**2

# Generate time and positions for object 2
t2 = 0
y2 = 0
while t2 <= t_final2:
    times2.append(t2)
    positions2.append(y2)
    t2 += dt2
    y2 = initial_velocity * t2 - 0.5 * g2 * t2**2

# Print header
print(f"For initial velocity of {initial_velocity:.2f} m/s:")
print("-----------------------------------------------------")
print(f"{'t (s)':<10}{'y1 (m)':<10}{'t (s)':<10}{'y2 (m)'}")
print(f"{'-'*10}{'-'*10}{'-'*10}{'-'*10}")

# Print table
for t1_val, y1_val, t2_val, y2_val in zip(times1, positions1, times2, positions2):
    print(f"{t1_val:<10.3f}{y1_val:<10.3f}{t2_val:<10.3f}{y2_val:<10.3f}")
