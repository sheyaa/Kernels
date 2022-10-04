import numpy as np

centers = [
    np.array([0,1]),
    np.array([2,0]),
    np.array([2,2])
    ]
weights = [1, 3, -2]

#for c in centers:
#    print(c)

for i in range( len(centers) ):
    print(centers[i])
    print(weights[i])

#for i,c in enumerate(centers):
#    print(i, c)

#for w,c in zip(weights, centers):
#    print(w, c)
    