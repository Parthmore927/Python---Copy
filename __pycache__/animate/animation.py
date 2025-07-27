import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create the circle
circle = plt.Circle((1, 5), 0.5, color='blue')
ax.add_patch(circle)

# Define animation function
def animate(frame):
    x = 1 + (frame / 50) * 8  # Moving from x=1 to x=9
    circle.set_center((x, 5))
    return circle,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=50, interval=50)

plt.show()
