import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Physical constants and parameters
k = 1e-6               # thermal diffusivity (m^2/s)
T0 = 10                # base temperature (°C)
A1 = 15                # annual amplitude (°C)
A2 = 7                 # diurnal amplitude (°C)

# Periods in seconds
P1 = 365 * 24 * 3600   # annual period
P2 = 24 * 3600         # diurnal period

# Angular frequencies
omega1 = 2 * np.pi / P1
omega2 = 2 * np.pi / P2

# Damping coefficients
a1 = np.sqrt(omega1 / (2 * k))
a2 = np.sqrt(omega2 / (2 * k))

# Depth grid
z = np.linspace(0, 2, 200)  # 0 to 2 meters

# Time step and total frames
dt = P2 / 10                # Δt = P2/10
n_frames = 300              # Number of frames

# Plot setup
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 2)
ax.set_ylim(T0 - A1 - A2 - 2, T0 + A1 + A2 + 2)
ax.set_xlabel('Depth (m)')
ax.set_ylabel('Temperature (°C)')
title = ax.set_title("")

# Initialization function
def init():
    line.set_data([], [])
    title.set_text("")
    return line, title

# Animation function
def animate(frame):
    t = frame * dt
    T = (
        T0
        + A1 * np.exp(-a1 * z) * np.sin(omega1 * t - a1 * z)
        + A2 * np.exp(-a2 * z) * np.sin(omega2 * t - a2 * z)
    )
    line.set_data(z, T)
    hours = (t % P2) / 3600
    days = int(t // P2)
    title.set_text(f"Day {days}, Hour {hours:.1f}")
    return line, title

# Animate
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=n_frames, interval=50, blit=True
)

plt.tight_layout()
plt.show()