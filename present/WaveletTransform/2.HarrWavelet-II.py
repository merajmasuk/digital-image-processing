from numpy import kron, array, eye, vstack
import numpy as np

H = array([[1, 1], [1, -1]])

for i in range(2):
	H = vstack([kron(H, [1, 1]), kron(eye(H.shape[0]), [1, -1])])

D = H.dot(H.T)
H = np.linalg.inv(np.sqrt(D)).dot(H)
w = (H.dot(v.T)).T

print(np.around(w, 2))
