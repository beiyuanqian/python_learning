# ImageEnhance模块包含了一些用于图像增强的类，它们分别为Color类、Brightness类、Contrast类和Sharpness
from PIL import Image, ImageEnhance

# im0的亮度是图像im的一半
im = Image.open(r"D:\PYproject\python_projectcase\123.png")
enhancer = ImageEnhance.Brightness(im)
im0 = enhancer.enhance(0.5)
im0.show()
