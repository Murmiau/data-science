%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


def draw_circle(r=1, x0=0, y0=0, color='black'):
    angle = np.linspace(0, 2 * np.pi, 360)

    x = np.add(r * np.cos(angle), x0)
    y = np.add(r * np.sin(angle), y0)

    plt.plot(x, y, color=color, linewidth=1)
    plt.gca().set_aspect('equal')


draw_circle(x0=0, y0=0)
