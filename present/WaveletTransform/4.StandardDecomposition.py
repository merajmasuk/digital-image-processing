import numpy as np

H = np.array([[1, 1], [1, -1]])

for i in range(2):
	H = np.vstack([np.kron(H, [1, 1]), np.kron(np.eye(H.shape[0]), [1, -1])])

K1 = np.kron(np.eye(32), H[0, :])
K2 = np.kron(np.eye(32), H[1, :])
K3 = np.kron(np.eye(32), H[2:4, :])
K4 = np.kron(np.eye(32), H[4:8, :])

H = np.vstack([K1, K2, K3, K4])
D = H.dot(H.T)

c = np.sqrt(np.linalg.inv(D)).dot(H)

cw = H.dot(H.dot(c.astype('float')).T).T
