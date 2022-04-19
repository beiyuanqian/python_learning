# ImageDraw模块为Image对象提供了基本的图形处理功能，例如可以为图像添加几何图形
from PIL import Image, ImageDraw

# 在原有的图像上画了两条对角线
im = Image.open(r"D:\PYproject\python_projectcase\123.png")
draw = ImageDraw.Draw(im)
print(im.size)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
im.show()
