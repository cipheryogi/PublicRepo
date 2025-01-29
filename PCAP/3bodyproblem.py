import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equations for the three-body problem
def three_body_equations(y, t):
    # y: array of positions and velocities
    # t: time
    # Define gravitational force equations here (e.g., Newton's law of gravitation)
    # Example: dydt = ...

    # Placeholder equations (replace with actual equations)
    G = 6.67430e-11  # Gravitational constant (m^3 kg^−1 s^−2)

    # Masses (arbitrary values)
    m1 = 1.0  # Mass of body 1
    m2 = 2.0  # Mass of body 2
    m3 = 3.0  # Mass of body 3

    # Positions and velocities
    x1, y1, z1, vx1, vy1, vz1 = y[0], y[1], y[2], y[3], y[4], y[5]
    x2, y2, z2, vx2, vy2, vz2 = y[6], y[7], y[8], y[9], y[10], y[11]
    x3, y3, z3, vx3, vy3, vz3 = y[12], y[13], y[14], y[15], y[16], y[17]

    # Compute distances and forces
    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2)
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2)

    # Gravitational forces
    f12 = G * m1 * m2 / r12**2
    f13 = G * m1 * m3 / r13**2
    f23 = G * m2 * m3 / r23**2

    # Equations of motion
    dydt = np.zeros_like(y)
    dydt[0:3] = [vx1, vy1, vz1]
    dydt[3:6] = [f12 * (x2 - x1) / r12, f12 * (y2 - y1) / r12, f12 * (z2 - z1) / r12]
    dydt[6:9] = [vx2, vy2, vz2]
    dydt[9:12] = [f13 * (x3 - x1) / r13, f13 * (y3 - y1) / r13, f13 * (z3 - z1) / r13]
    dydt[12:15] = [vx3, vy3, vz3]
    dydt[15:18] = [f23 * (x3 - x2) / r23, f23 * (y3 - y2) / r23, f23 * (z3 - z2) / r23]

    return dydt

# Initial conditions (arbitrary values)
y0 = np.array([
    1.0, 0.0, 0.0, 0.0, 0.5, 0.0, -1.0, 0.0, 0.0, 0.0, 0.5, 0.0,
    0.0, 1.0, 0.0, 0.0, -0.5, 0.0
])
t = np.linspace(0, 100, 1000)  # Time span

# Solve the differential equations
sol = odeint(three_body_equations, y0, t)

# Extract positions (x, y, z) for each body
x1, y1, z1 = sol[:, 0], sol[:, 1], sol[:, 2]
x2, y2, z2 = sol[:, 6], sol[:, 7], sol[:, 8]
x3, y3, z3 = sol[:, 12], sol[:, 13], sol[:, 14]


# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(x1, y1, z1, label="Body 1")
ax.plot(x2, y2, z2, label="Body 2")
ax.plot(x3, y3, z3, label="Body 3")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

# Save the plot to an HTML file (you can customize this part)
plt.savefig("three_body_plot.png")
plt.close()

# Now create an HTML page with an <img> tag linking to "three_body_plot.png"
# You can also add more styling and interactivity using JavaScript if needed.
