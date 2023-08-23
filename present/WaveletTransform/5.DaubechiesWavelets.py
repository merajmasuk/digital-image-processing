import numpy as np
import rwt
import matplotlib.pyplot as plt

t = np.array([0]*512); t[5]=1
td = rwt.idwt(t, h, 9)[0]
plt.plot(np.arrange(512), td)
