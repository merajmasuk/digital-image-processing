import cv2
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt


# fix qt package conflict error, import system qt instead of opencv qt plugin
import os
import platform

if platform.system() == 'Linux':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/usr/share/qt'

img = io.imread('../Dataset/4.2.05.tiff')

def add_salt_and_pepper_noise(image, amount=0.05):
    height, width = image.shape[:2]
    num_pixels = int(amount * height * width)

    for _ in range(num_pixels // 2):
        x, y = np.random.randint(0, width), np.random.randint(0, height)
        image[y, x] = 255

    for _ in range(num_pixels // 2):
        x, y = np.random.randint(0, width), np.random.randint(0, height)
        image[y, x] = 0

    return image

img_noisy = add_salt_and_pepper_noise(np.copy(img))


def median_filter(image, kernel_size):
    height, width, channels = image.shape
    pad = kernel_size // 2
    filtered_image = np.zeros_like(image)

    for c in range(channels):
        for y in range(pad, height - pad):
            for x in range(pad, width - pad):
                region = image[y - pad : y + pad + 1, x - pad : x + pad + 1, c]
                filtered_image[y, x, c] = np.median(region)

    return filtered_image

# img_filtered = median_filter(img_noisy, 5)
img_filtered = cv2.medianBlur(img_noisy, 5)


fig, axs = plt.subplots(1, 3, figsize=(10, 5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(img_noisy, cmap='gray')
axs[1].set_title('Noisy Image (Salt & Pepper)')
axs[1].axis('off')

axs[2].imshow(img_filtered, cmap='gray')
axs[2].set_title('Denoised Image (Median Filter)')
axs[2].axis('off')

plt.tight_layout()
plt.show()

