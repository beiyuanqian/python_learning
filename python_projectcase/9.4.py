# 用python生成验证码图片
import random, string, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

font_path = r"C:\Windows\Fonts\simfang.ttf"
# 生成几位数的验证码
number = 4
# 生成验证码图片的高度和宽度
size = (80, 30)
# 背景颜色，默认为白色
bgcolor = (255, 255, 255)
# 字体颜色，默认为蓝色
fontcolor = (0, 0, 255)
# 干扰线颜色，默认为红色
linecolor = (255, 0, 0)
# 是否要加入干扰线
draw_line = True
# 加入干扰线条数的上/下限
line_number = (1, 5)


# 用来随机生成一个字符串
def gene_text():
    # source=list(string.letters)
    # source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    #           'v', 'w', 'x', 'y', 'z']
    source = list(string.ascii_letters)
    for index in range(0, 10):
        source.append(str(index))
    return ''.join(random.sample(source, number))


# 用来绘制干扰线
def gene_line(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=linecolor)


# 生成验证码
def gene_code():
    # 宽和高
    width, height = size
    # 创建图片
    image = Image.new('RGBA', (width, height), bgcolor)
    # 验证码的字体
    font = ImageFont.truetype(font_path, 25)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 生成字符串
    text = gene_text()
    font_width, font_height = font.getsize(text)
    print(font_width,font_height)
    # 填充字符串
    draw.text(((width - font_width) / number, (height - font_height) / number), text, font=font, fill=fontcolor)
    if draw_line:
        gene_line(draw, width, height)
    # 创建扭曲
    image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
    # 滤镜，边界加强
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    # 保存验证码图片
    image.save('idencode.png')


if __name__ == "__main__":
    gene_code()
