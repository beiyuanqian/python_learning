from PIL import Image,ImageFilter
im=Image.open(r"D:\PYproject\python_projectcase\123.png")
imout=im.filter(ImageFilter.BLUR)
print(imout.size)
imout.show()