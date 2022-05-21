from pylab import *
from mpl_toolkits.mplot3d import Axes3D


def draw_fig():
    fig = figure()
    ax = Axes3D(fig)
    coefs = (0.01, 0.02, 0.02)
    rx, ry, rz = 1 / np.sqrt(coefs)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))
    X = np.arange(-7, 7, 0.5)
    Y = np.arange(-7, 7, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = np.sqrt(4. * (X ** 2 + Y ** 2) / 1. + 1)
    ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, color='red', linewidth=1)
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5, color='green')
    max_radius = max(rx, ry, rz)
    for axis in 'xyz':
        getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))
    ax.scatter(0, 0, 0, 'z', 50, 'blue')
    show()


draw_fig()
