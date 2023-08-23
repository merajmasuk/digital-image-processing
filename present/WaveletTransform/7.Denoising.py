import numpy as np
import rwt
import io

f = ut.img_as_float(io.imread('fledgling.png'))
fg = ut.random_noise(f, 'gaussian')
fw = rwt.dwt(fg, h, 4)[0]
fw[np.where(abs(fw)<=0.4)] = 0
fi = rwt.idwt(fw, h, 4)
io.imshow(fi[0])

