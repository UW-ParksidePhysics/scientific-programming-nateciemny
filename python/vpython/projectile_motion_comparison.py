import vpython as vp
import numpy as np

# Variables
angle1 = np.pi / 4
angle2 = np.pi / 2 - angle1
speed = 15
gravities = {'Earth': 9.8, 'Mars': 3.7, 'Moon': 1.6}
colors = {
    'Earth': vp.color.green,
    'Mars': vp.color.red,
    'Moon': vp.color.gray(0.5)
}
ball_colors = {
    'Earth': vp.color.blue,
    'Mars': vp.color.magenta,
    'Moon': vp.color.white
}
labels = {
    'Earth': "EARTH",
    'Mars': "MARS",
    'Moon': "MOON"
}

# Settings
dt = 0.01
field_width = 20
field_depth = 5
field_height = 0.5
initial_height = 0.5
pause_time = 1  # time between rounds

# Make the fields and the balls
fields = {}
balls = {}
texts = {}
positions = [-25, 0, 25]
scene = vp.canvas(title="Projectile Motion Comparison", width=1200, height=600, background=vp.color.black)

for i, (planet, g) in enumerate(gravities.items()):
    x_offset = positions[i]

    # Field box
    field = vp.box(pos=vp.vector(x_offset, 0, 0), size=vp.vector(field_width, field_height, field_depth),
                   color=colors[planet])
    fields[planet] = field

    # 3D text label
    texts[planet] = vp.text(text=labels[planet], pos=field.pos + vp.vector(0, -1, 0), height=1, depth=0.2,
                            color=colors[planet], align='center')


def run_simulation(launch_angle):
    # Create balls
    active_balls = {}
    for i, (planet, g) in enumerate(gravities.items()):
        x_offset = positions[i]
        pos = vp.vector(x_offset - field_width / 2, initial_height, 0)
        vx = speed * np.cos(launch_angle)
        vz = speed * np.sin(launch_angle)
        vel = vp.vector(vx, 0, vz)
        ball = vp.sphere(pos=pos, radius=0.4, color=ball_colors[planet], make_trail=True)
        active_balls[planet] = {'ball': ball, 'vel': vel, 'g': g}

    t = 0
    running = True
    while running:
        vp.rate(100)
        t += dt
        running = False
        for planet, data in active_balls.items():
            ball = data['ball']
            vel = data['vel']
            g = data['g']

            # Position
            vel.z -= g * dt
            ball.pos += vel * dt

            # Check if it's still in the air
            if ball.pos.z > 0:
                running = True

    vp.sleep(pause_time)

    for data in active_balls.values():
        data['ball'].visible = False


# Run first simulation with angle θ
run_simulation(angle1)

# Run second simulation with π/2 - θ
run_simulation(angle2)
