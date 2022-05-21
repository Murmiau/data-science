%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


def draw_hyperbola(a=1, b=1, x_range=[-3, 3], color='black'):
    epsilon = np.finfo(float).eps
    f0 = epsilon + a
    x1 = np.linspace(x_range[0], f0, (x_range[1] - x_range[0]) * 1000)
    x2 = np.linspace(f0, x_range[1], (x_range[1] - x_range[0]) * 1000)

    f = lambda x: np.sqrt((x ** 2 / a ** 2) - 1) / b

    y1 = np.array([f(v) for v in x1])
    y2 = np.array([f(v) for v in x2])
    y3 = np.array([-f(v) for v in x1])
    y4 = np.array([-f(v) for v in x2])

    plt.plot(x1, y1, color=color, linewidth=1)
    plt.plot(x2, y2, color=color, linewidth=1)
    plt.plot(x1, y3, color=color, linewidth=1)
    plt.plot(x2, y4, color=color, linewidth=1)
    plt.gca().set_aspect('equal')


draw_hyperbola()
