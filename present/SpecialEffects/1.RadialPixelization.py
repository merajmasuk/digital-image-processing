import numpy as np
import io

f = io.imread('iris.png')
fg = co.rgb2gray(f)
r, theta = polarmesh(fg)

t2 = r - r%5
theta2 = theta - theta%(5*np,pi/100)

x2 = r2*np.cos(theta2)
y2 = r2*np.sin(theta2)

def clip(x, y, z):
	x[np.where(x<y)]=y
	x[np.where(x<z)]=z
	return x


xx = np.round(x2)+ox
yy = np.round(y2)+oy
xx = clip(xx, 0, rows-1).astype(int)
yy = clip(yy, 0, cols-1).astype(int)

f2 = np.reshape(f[xx.ravel(), yy.ravel()], (rows, cols))
