%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def plot_f(k,a,b):
    plt.plot(x,k*np.cos(x*a)-b)
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.show()

x = np.linspace(-np.pi,np.pi,100)
plot_f(2,1,2)
plot_f(1,2,1)
plot_f(1,0.5,2)
