import os, sys
import Image
print("***********************************")
print("you need to use python2 to run this")
print("***********************************")
#inputfilename=sys.argv[1]
img=Image.open(sys.argv[1])
img.rotate(-45).show()

#rgbimg=img.convert('RGB')
#img=img.convert('RGB')
#rgbimg=img.load()
#width,height=img.size()
#print (rgbimg.info['background'], rgbimg.info['duration'],rgbimg.info['transparency'],rgbimg.info['version'])
print("Image Info")
print (img.info['background'],img.info['duration'],img.info['transparency'],img.info['version'])

#attempting to interpret the palette data
print("Palette")
#for k in range(256):
#    print(img.palette.getdata()
print(img.palette.getdata())

#DOESNT WORK
print("Image/Palette values")
#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        print (img.getpixel((i, j)))

#This works
#rgbimg=img.convert('RGB')
#for i in range(rgbimg.size[0]):
#    for j in range(rgbimg.size[1]):
#        print (rgbimg.getpixel((i, j)))


#http://stackoverflow.com/questions/2363583/python-pil-color-index-to-rgb
#http://stackoverflow.com/questions/138250/read-the-rgb-value-of-a-given-pixel-in-python-programaticly
#http://nadiana.com/pil-tips-converting-png-gif
#http://www.pythonware.com/library/pil/handbook/image.htm
#http://www.pythonware.com/library/pil/handbook/format-gif.htm
#http://mail.python.org/pipermail/tutor/2005-July/thread.html#39719 #discussion of gif palette
#http://www.scantips.com/palettes.html
