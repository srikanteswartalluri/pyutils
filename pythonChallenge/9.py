__author__ = 'talluri'
from PIL import Image


img = Image.new('RGB', (640, 480))
dots = open('dots.txt', 'r').read().replace('\n', '').split(',')
pixels = [(int(dots[i]), int(dots[i+1])) for i in range(0, len(dots)-1, 2)]

for pixel in pixels:
    img.putpixel(pixel, 255)

img.save('connected_dots.png')