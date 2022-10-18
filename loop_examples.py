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
    

#for j in range(1,4):
 #   sum(i)
#    print

S=0
for j in range( len(weights) ):
    S=S + (weights[j])
    
print(S)


###############################################
from numpy import linalg as LA

x = [
     np.array([1,1]),
     np.array([0,2]),
     np.array([2,0]),
     np.array([2,1])]

for i in range(len(centers)):
    for k in range(len(x)):
        D = LA.norm (x[0] - centers[i])
print("D =", D)