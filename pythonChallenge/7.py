__author__ = 'talluri'


from PIL import Image
import re
img = Image.open('/Users/talluri/Downloads/oxygen.png')
y = img.size[1]/2

string = "".join([chr(img.getpixel((x, y))[0]) for x in range(0, img.size[0], 7)])

listofnum = re.findall(r'\d{3}', string)

print "".join(chr(int(i)) for i in listofnum)


