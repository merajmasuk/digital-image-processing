import cv2
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

# fix qt package conflict error, import system qt instead of opencv qt plugin
import os
import platform

if platform.system() == 'Linux':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/usr/share/qt'

img = io.imread('../Dataset/4.2.05.tiff', as_gray=True)


def prewitt_edge_detection(image):
    prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    grad_x = cv2.filter2D(image, -1, prewitt_x)
    grad_y = cv2.filter2D(image, -1, prewitt_y)

    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

    return gradient_magnitude


prewitt_edges = prewitt_edge_detection(np.copy(img))

fig, axs = plt.subplots(1, 2, figsize=(15, 5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(prewitt_edges, cmap='gray')
axs[1].set_title('Prewitt Edge Detection')
axs[1].axis('off')

plt.tight_layout()
plt.show()
