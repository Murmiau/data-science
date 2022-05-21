%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5)
k1 = 1
k2 = 2
plt.plot(x, np.cos(x*k1), marker = "+")
plt.plot(x, np.cos(x*k2), marker = "x")
plt.show()