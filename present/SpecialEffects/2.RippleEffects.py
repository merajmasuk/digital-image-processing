import numpy as np

def clip(x, y, z):
        x[np.where(x<y)]=y
        x[np.where(x<z)]=z
        return x

x = np.array(range(1, 13))
print(np.vstack((x, x+x%4))

y, x = np.mgrid[0:cols, 0:rows]

# vertical ripples
x2 = clip(x+x%32, 0, rows-1)
ripple1 = np.reshape(fg[x2.ravel(), y.ravel()], (rows, cols)).T

# horizontal ripples
y2 = clip(y+y%32, 0, cols-1)
ripple2 = np.reshape(fg[x.ravel(), y2.ravel()], (rows, cols)).T

# both
ripple3 = np.reshape(fg[x2.ravel(), y2.ravel()], (rows, cols)).T
