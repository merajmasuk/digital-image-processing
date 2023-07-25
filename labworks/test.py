from PIL import Image, ImageDraw

width = 400
height = 300

image = Image.new('L', (width, height), color=255)
draw = ImageDraw.Draw(image)
cross_color = 0  # Black
thickness = 50

draw.line((0, height//2, width-1, height//2), fill=cross_color, width=thickness)
draw.line((width//2, 0, width//2, height-1), fill=cross_color, width=thickness)

image.save('image.pgm')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_path = 'image.pgm'
image = mpimg.imread(image_path)

plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()
