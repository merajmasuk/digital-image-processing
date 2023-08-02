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

def apply_periodic_noise(image, amplitude=1, frequency=100):
    height, width = image.shape[:2]

    x = np.arange(0, width)
    y = np.arange(0, height)
    X, Y = np.meshgrid(x, y)
    noise_pattern = amplitude * np.sin(2 * np.pi * frequency * X / width)

    noisy_img = np.clip(image + noise_pattern, 0, 255).astype(np.uint8)

    return noisy_img


img_noisy = apply_periodic_noise(np.copy(img))


def remove_periodic_noise(image, frequency_x, frequency_y, amp=20):
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)

    rows, cols = image.shape
    center_x, center_y = rows // 2, cols // 2

    mask = np.ones_like(image)
    mask[center_x - amp:center_x + amp, center_y - amp:center_y + amp] = 0
    mask[center_x - amp + frequency_x:center_x + amp + frequency_x,
         center_y - amp + frequency_y:center_y + amp + frequency_y] = 1
    mask[center_x - amp - frequency_x:center_x + amp - frequency_x,
         center_y - amp - frequency_y:center_y + amp - frequency_y] = 1

    f_shift_filtered = f_shift * mask

    f_transform_filtered = np.fft.ifftshift(f_shift_filtered)
    image_filtered = np.fft.ifft2(f_transform_filtered).real

    return image_filtered


img_filtered = remove_periodic_noise(np.copy(img), frequency_x=100, frequency_y=100, amp=1)

fig, axs = plt.subplots(1, 3, figsize=(10, 5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(img_noisy, cmap='gray')
axs[1].set_title('Noisy Image (Periodic Noise)')
axs[1].axis('off')

axs[2].imshow(img_filtered, cmap='gray')
axs[2].set_title('Denoised Image (Fourier Transform)')
axs[2].axis('off')

plt.tight_layout()
plt.show()

