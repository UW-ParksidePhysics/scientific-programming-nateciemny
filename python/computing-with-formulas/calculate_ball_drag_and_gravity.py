import math

# Define constants and variables
drag_coefficient = 0.2  # CD
air_density = 1.2  # ρ (kg/m^3)
ball_radius = 0.11  # a (m)
ball_mass = 0.43  # m (kg)
gravitational_acceleration = 9.81  # g (m/s^2)

# Calculate cross-sectional area of the ball (A = πa^2)
cross_area = math.pi * ball_radius ** 2


# Function to calculate drag force and gravity force
def calculate_forces(ball_velocity_kmh):
    # Convert velocity from km/h to m/s
    ball_velocity = ball_velocity_kmh * 1000 / 3600

    # Calculate drag force (Fd = 0.5 * CD * ρ * A * v^2)
    drag_force = 0.5 * drag_coefficient * air_density * cross_area * ball_velocity ** 2

    # Calculate gravity force (Fg = m * g)
    gravitational_force = ball_mass * gravitational_acceleration

    # Calculate ratio of drag force to gravity force
    ratio = drag_force / gravitational_force

    # Print results
    print(f"\nBall Velocity: {ball_velocity_kmh} km/h ({ball_velocity:.2f} m/s)")
    print(f"Drag Force (Fd): {drag_force:.1f} N")
    print(f"Gravity Force (Fg): {gravitational_force:.1f} N")
    print(f"Ratio (Fd / Fg): {ratio:.2f}")


# Calculate for hard kick (120 km/h) and soft kick (10 km/h)
calculate_forces(120)  # Hard kick
calculate_forces(10)  # Soft kick