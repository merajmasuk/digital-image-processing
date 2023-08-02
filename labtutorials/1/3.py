import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

# fix qt package conflict error, import system qt instead of opencv qt plugin
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/usr/share/qt'

color_image = io.imread("..//Dataset//4.2.05.tiff")
hsv_image = color.rgb2hsv(color_image)

red_channel, green_channel, blue_channel = cv2.split(color_image)
hue_channel, sat_channel, value_channel = cv2.split(hsv_image)


fig, axs = plt.subplots(4, 3, figsize=(10, 8))

axs[0, 0].axis('off')

axs[0, 1].imshow(color_image)
axs[0, 1].set_title('RGB Image')

axs[0, 2].axis('off')

axs[1, 0].imshow(red_channel, cmap='gray')
axs[1, 0].set_title('Red Channel')

axs[1, 1].imshow(green_channel, cmap='gray')
axs[1, 1].set_title('Green Channel')

axs[1, 2].imshow(blue_channel, cmap='gray')
axs[1, 2].set_title('Blue Channel')

axs[2, 0].axis('off')

axs[2, 1].imshow(hsv_image)
axs[2, 1].set_title('HSV Image')

axs[2, 2].axis('off')

axs[3, 0].imshow(hue_channel, cmap='gray')
axs[3, 0].set_title('Hue Channel')

axs[3, 1].imshow(sat_channel, cmap='gray')
axs[3, 1].set_title('Saturation Channel')

axs[3, 2].imshow(value_channel, cmap='gray')
axs[3, 2].set_title('Value Channel')

plt.tight_layout()
plt.show()
