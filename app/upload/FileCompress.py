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

def ArticleCover(files):
    """图片处理:封面裁剪"""
    templateW = 390
    templateH = 230

    file = Image.open(files)
    source_w = [0, file.size[0]]
    source_h = [1, file.size[1]]

    # 取出源文件最短的一条边
    minlength = source_w if source_w[1] < source_h[1] else source_h

    if minlength[0] == 1:
        if source_w[1] > source_h[1]:
            rate = float(390) / float(source_w[1])
        else:
            rate = float(230) / float(source_h[1])
            
        new_size = (int(source_w[1] * rate), int(source_h[1] * rate))

        file = file.resize(new_size,Image.ANTIALIAS)
        
    else:

        # 切割高度比例
        cropH = minlength[1] / 1.665

        # 裁剪
        file = file.crop((0, 0, minlength[1], cropH))

        # 高质量压缩
        file = file.resize((templateW, templateH),Image.ANTIALIAS)

    return file.crop((0, 0, 390, 230))