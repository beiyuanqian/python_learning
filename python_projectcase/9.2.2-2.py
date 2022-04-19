from PIL import Image, ImageChops

im = Image.open(r"D:\PYproject\python_projectcase\123.png")
# 复制图像，返回给定图像的副本
im_dup = ImageChops.duplicate(im)
# 输出模式：“RGB”
print(im_dup.mode)
# 返回两幅图像之间像素差的绝对值形成的图像
im_diff = ImageChops.difference(im, im_dup)
im_diff.show()
