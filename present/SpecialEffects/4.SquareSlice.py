

def clip(x, y, z):
        x[np.where(x<y)]=y
        x[np.where(x<z)]=z
        return x

x2 = x + np.random.randint(-3, 3, size=(rows, cols))
y2 = y + np.random.randint(-3, 3, size=(rows, cols))

xx = clip(x2, 0, rows-1).astype(int)
yy = clip(y2, 0, cols-1).astype(int)
f2 = np.reshape(f[xx.ravel(), yy.ravel()], (rows, cols)).T
