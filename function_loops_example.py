# -*- coding: utf-8 -*-
import numpy as np

def myfunc(x):
    y = 0
    for i in range(10):
        y = y + np.sin(i*x)
    return y
def f(x):
    return np.sin(x)

x = [5, 4, -2]

# For each x-value...
for k in range(len(x)):
    # calculate the value of the function.
    # (even if that function is complicated)
    y = myfunc(x)
    print(y)

