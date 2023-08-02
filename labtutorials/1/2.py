import cv2
import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

# fix qt package conflict error, import system qt instead of opencv qt plugin
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/usr/share/qt'

img01= io.imread('..//Dataset//4.2.05.tiff')
# io.imshow(img01)
# io.show()

# Gaussian
f = ndi.gaussian_filter(img01, 0.5)
# io.imshow(f)
# io.show()

# Laplacian
r, g, b = cv2.split(img01)

laplacian_r = cv2.Laplacian(r, cv2.CV_64F)
laplacian_g = cv2.Laplacian(g, cv2.CV_64F)
laplacian_b = cv2.Laplacian(b, cv2.CV_64F)

laplacian_rgb = cv2.merge([laplacian_r, laplacian_g, laplacian_b])
laplacian_rgb = np.clip(laplacian_rgb, 0, 255).astype(np.uint8)

stacked_images = np.hstack((img01, f, laplacian_rgb))
io.imshow(stacked_images)
io.show()
