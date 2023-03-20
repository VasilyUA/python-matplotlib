import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2 * np.pi, 1000)

x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

heart, = ax.plot(x, y, color='red')

def update(frame):
    heart.set_data(x * (1 + 0.1 * np.sin(frame / 10)), y * (1 + 0.1 * np.sin(frame / 10)))
    return heart,

ani = FuncAnimation(fig, update, frames=range(0, 200), interval=50, blit=True)

plt.show()