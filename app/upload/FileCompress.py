from PIL import Image

def HeadImg(files):
    """图片处理:头像裁剪"""
    
    file = Image.open(files)

    topw = [0, 0]

    xl, yl = file.size
    print(xl, yl)

    if xl > yl:
        topw = [yl, 1]
        print(topw)
    else:
        topw = [xl, 0]
        print(topw)

    px = topw[0]

    file = file.crop((0, 0, px, px))

    print(file.size)
    return file
