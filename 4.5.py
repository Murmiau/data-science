my_list = [n for n in range(100, 1001) if n % 2 == 0]
print(my_list)
from functools import reduce
def my_func(n_p, n):
    return n_p * n
print(reduce(my_func, my_list))