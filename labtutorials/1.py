import cv2
import numpy as np
import skimage.io as io
import skimage.color as color
import skimage.exposure as ex
import matplotlib.pyplot as plt

# fix qt package conflict error, import system qt instead of opencv qt plugin
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/usr/share/qt'

img01= io.imread('..//Dataset//4.2.05.tiff')
io.imshow(img01)
io.show()

f = plt.figure()
f.show(plt.hist(img01.flatten(), bins=256))
plt.show()

r, g, b = cv2.split(img01)
r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)
img02 = cv2.merge([r_eq, g_eq, b_eq])

# img02 = cv2.equalizeHist(img01)
io.imshow(img02)
io.show()

f = plt.figure()
f.show(plt.hist(img02.flatten(), bins=256))
plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].imshow(img01)
axs[0, 0].set_title('Original Image')

axs[0, 1].hist(img01.flatten(), bins=256)
axs[0, 1].set_title('Original Histogram')

axs[1, 0].imshow(img02)
axs[1, 0].set_title('Equalized Image')

axs[1, 1].hist(img02.flatten(), bins=256)
axs[1, 1].set_title('Equalized Histogram')

plt.tight_layout()
plt.show()
