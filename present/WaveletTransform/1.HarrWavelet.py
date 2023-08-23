from numpy import kron, array, eye, vstack

v = array([71, 67, 24, 26, 36, 32, 14, 18])
H = vstack([kron(eye(4), [1, 1]), kron(eye(4), [1, -1])])
w = (H.dot(v.T)).T

print(w)
