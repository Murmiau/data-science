from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def draw_parallel_planes(A=0, B=0, C=1, D=0, z_offset=0):
    fig = figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.5)
    Y = np.arange(-4, 4, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = (A*X + B*Y + D)/C
    Z_2 = (A*X + B*Y + D)/C + z_offset
    ax.plot_wireframe(X, Y, Z, color='red')
    ax.plot_wireframe(X, Y, Z_2, color='green')
    ax.scatter(0, 0, 0, 'z', 50, 'blue')
    show()

draw_parallel_planes(0, 1, z_offset=2)
