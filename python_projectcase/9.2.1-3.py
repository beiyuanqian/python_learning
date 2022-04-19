import qrcode
import qrcode.image.svg

if method == "basic":
    # 简单的工厂，只有一套
    factory = qrcode.image.svg.SvgImage
elif method == "fragment":
    # 碎片工厂（也只有一组矩形）
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # 组合路径工厂，修复缩放时可能出现的空白
    factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make("xinxingzhao", image_factory=factory)
