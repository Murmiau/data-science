%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def vector_size(vs):
    sqr_sum = 0.0
    for x in vs:
        sqr_sum += x**2
    return np.sqrt(sqr_sum)
vector_size([10, 10, 10])
