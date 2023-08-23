import io


def mymode(x):
	return sc.stats.mode(x, axis=None)[0][0]

f2 = ndi.generic_filter(fg, mymode, size=(9,9))

u = fg>0.5
sol = u*fg + (1-u)*(1-fg)

io.imshow(col, vmin=0, vmax=1)
io.imshow(sol)
