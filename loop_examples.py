import numpy as np
from numpy import linalg as LA
###############################################
#DEFINE FUNC
# np.piecewise?
def phi(x, T=1):
    result = np.piecewise(
        x,
        [x <= T, x>T],
        [1, 0]
        )
    return result

#x array
x = [
     np.array([1,1]),
     np.array([0,2]),
     np.array([2,0]),
     np.array([2,1])]

#centers
c = [
     np.array([0,1]),
     np.array([2,0]),
     np.array([2,2])]


#weights
w= np.array([1, 3, -2])

y = np.zeros(len(x))  #for each center for i


for k in range(len(x)): #for each x 
    for i in range(len(c)):  #for each center
        D = LA.norm (x[k] - c[i])
        
        y[k] = y[k] + (w[i] * phi(D))
        
        print("D =", D)
    print("y=", y)
    print("k=", k)
   # print("center =", c[i])
#print("x-value =", x[k])
        
 


 
    
 
    
 
    
############################################### 
    #for c in centers:
#    print(c)
'''
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
    #S=S + (weights[j])
    
print(S)
'''