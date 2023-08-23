import numpy as np
import io

f = io.imread('iris.png')
K = 150; phi = theta + r/K
r2 = r + r%30

twirl = np.zeroes_like(f)
ripple = np.zeroes_like(f)

for i in range(3):
	twirl[:,:,1] = polar2im(f[:,:,i], r, phi)
	ripple[:,:,1] = polar2im(f[:,:,i], r2, theta)
