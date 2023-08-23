import rwt

h, g = rwt.daubcqf(2)

print(rwt.dwt(v, h, 1)[0])
print(rwt.dwt(v, h, 3)[0])

h = np.array([1, 1]).astype('float')
vw = rwt.dwt(v, h, 3)[0]

print(vw[0])

hi = np.array([0.5, 0.5]).astype('float')

print(rwt.idwt(vw[0], hi, 3)[0])
