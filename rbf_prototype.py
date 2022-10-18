
import numpy as np

# np.piecewise?
def phi(x, T=1):
    result = np.piecewise(
        x,
        [x <= T, x>T],
        [1, 0]
        )
    return result
#
#################

x = np.array([1,1])

# Define W

# Define C


y = np.zeros( x.shape )
for i in range(3):
    y = y + W[i] * phi( np.linalg.norm(x - C[i]) )
print(y)
