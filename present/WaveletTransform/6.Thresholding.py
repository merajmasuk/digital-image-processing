import numpy as np
import rwt
import io

cw = mdwt(c.astype(double), h, 8)
len(np.where(abs(cw)<=30)[0])

cw[np.where(abs(cw)<=30)] = 0
cw = round(cw)
ci = rwt.idwt(cw, h, 8)

io.imshow(ci)

cw = rwt.dwt(c.astype(double), h, 8)
length(find(abs(cw)<=50))
cw[np.where(abs(cw)<=50)] = 0
cw = np.round(cw)
ci = rwt.idwt(cw, h, 8)

io.imshow(ci)

