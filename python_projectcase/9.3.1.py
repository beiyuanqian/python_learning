# 生成带有图标的二维码
import qrcode
from PIL import Image
import os, sys


def gen_qrcode(string, path, logo=""):
    """
    生成中间带logo的二维码，需要安装qrcode、PIL库
    :param string: 二维码字符串
    :param path: 生成的二维码保存路径
    :param logo: 文件路径
    :return: None
    """
    # 初步生成二维码图像
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=1)
    qr.add_data(string)
    qr.make(fit=True)
    # 获得Image实例并把颜色模式转换为RGBA
    img = qr.make_image()
    img = img.convert("RGBA")
    if logo and os.path.exists(logo):
        try:
            # 打开填充的logo文件
            icon = Image.open(logo)
            img_w, img_h = img.size
        except Exception as e:
            print(e)
            sys.exit(1)
        factor = 4
        # 计算logo的尺寸
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        # 计算并重新设置logo文件的尺寸
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        # 计算logo的位置，并复制到二维码图像中
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        # 保存二维码
        img.save(path)


if __name__ == "__main__":
    info = "http://www.zut.edu.cn"
    # 生成的带有图标的二维码图片
    pic_path = "qrcode.png"
    # 用于填充的图标
    logo_path = "123.png"
    gen_qrcode(info, pic_path, logo_path)
