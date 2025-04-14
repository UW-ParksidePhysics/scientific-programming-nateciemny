import vpython as vp

# Wall
wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

# Ball 1: starts at bottom
initial_position1 = vp.vector(-10., wall.pos.y - wall.size.y / 2, 0.)
initial_velocity1 = vp.vector(20., 5., 0.)
ball1 = vp.sphere(pos=initial_position1, radius=0.5, color=vp.color.blue, make_trail=True)

# Ball 2: starts at top
initial_position2 = vp.vector(-10., wall.pos.y + wall.size.y / 2, 0.)
initial_velocity2 = vp.vector(20., -5., 0.)
ball2 = vp.sphere(pos=initial_position2, radius=0.5, color=vp.color.green, make_trail=True)

# Time
animation_time_step = 0.01  # seconds
rate_of_animation = 1 / animation_time_step
time_step = 0.005
stop_time = 1.

# Initial velocities
ball1_velocity = initial_velocity1
ball2_velocity = initial_velocity2

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)

    # Ball 1 bounce
    if abs(ball1.pos.x - wall.pos.x) <= (ball1.radius + wall.size.x / 2) and ball1_velocity.x > 0:
        ball1_velocity.x = -ball1_velocity.x
    # Ball 2 bounce
    if abs(ball2.pos.x - wall.pos.x) <= (ball2.radius + wall.size.x / 2) and ball2_velocity.x > 0:
        ball2_velocity.x = -ball2_velocity.x

    # Positions
    ball1.pos += ball1_velocity * time_step
    ball2.pos += ball2_velocity * time_step

    time += time_step
