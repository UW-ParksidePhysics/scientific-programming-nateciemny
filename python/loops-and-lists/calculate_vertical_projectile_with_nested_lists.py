# Values for t and y
times = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
positions = [0.0, 1.5, 2.9, 4.1, 5.0, 5.6, 6.1]

# a. Store times and positions in nested list
times_positions = [times, positions]

# Print table header
print("For time (t) in [s] and position (y) in [m]:")
print(f"{'t (s)':<10} {'y (m)'}")
print("-" * 20)

# b. loop to print t and y values
for t, y in zip(times_positions[0], times_positions[1]):
    print(f"{t:<10.2f} {y:.2f}")

# Create list
time_positions_rows = [[t, y] for t, y in zip(times_positions[0], times_positions[1])]

# Print tables
print("\nTime and Position as rows:")
print(f"{'t (s)':<10} {'y (m)'}")
print("-" * 20)

for row in time_positions_rows:
    print(f"{row[0]:<10.2f} {row[1]:.2f}")
