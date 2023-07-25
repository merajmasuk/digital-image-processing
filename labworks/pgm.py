from PIL import Image, ImageDraw

image_path = '../Dataset/house.tiff'
image = Image.open(image_path)
image = image.convert('RGB')

draw = ImageDraw.Draw(image)

width, height = image.size

cross_color = (0, 0, 0) #black
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

thickness = 10
margin = 25

char_width = (width-margin*4)//3

top = margin
middle = height//2
bottom = height-1-margin

# 1
right = margin+char_width
draw.line((right, margin, right, height-1-margin), fill=red, width=thickness)

# 2
left = 2*margin+char_width
right = 2*(margin+char_width)
draw.line((left, top, right, top), fill=green, width=thickness)
draw.line((right, top, right, middle), fill=green, width=thickness)
draw.line((left, middle, right, middle), fill=green, width=thickness)
draw.line((left, middle, left, bottom), fill=green, width=thickness)
draw.line((left, bottom, right, bottom), fill=green, width=thickness)

# 3
left = 3*margin+2*char_width
right = 3*(margin+char_width)
draw.line((left, top, right, top), fill=blue, width=thickness)
draw.line((right, top, right, middle), fill=blue, width=thickness)
draw.line((left, middle, right, middle), fill=blue, width=thickness)
draw.line((right, middle, right, bottom), fill=blue, width=thickness)
draw.line((left, bottom, right, bottom), fill=blue, width=thickness)

output_path = 'output.pgm'
image.save(output_path)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_path = 'output.pgm'
image = mpimg.imread(image_path)

plt.imshow(image)
plt.axis('off')
plt.show()
