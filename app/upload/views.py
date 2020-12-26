import hashlib
import os
import random
from datetime import datetime
from io import *
# from manage import RUN_CONFIG
from app.Config import config
from app.RAM import AppRAM

from app.upload import FileCompress

"""
    关于 UPLOADFILE_CONFIG的用法
    key: 上传文件的时候必须附带的参数uploadKey : 此处设置的key
    value: 上传的文件根据key获取储存的路径 比方说 'head':'image', 表示携带head上传的文件需要储存到image路径下
"""
UPLOADFILE_CONFIG = {
    'userhead': '/head',
}

def CreateNewFilename(ext):
    """生成新的随机文件名
    Args:
        ext: str, 文件后缀名

    Returns:
        生成的随机字符串 + 后缀名

    """
    return datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '{:03d}'.format(random.randint(0, 999)) + ext


def QueryFileName(filestr):
    """分割文件名

    Args:
        filestr: str, 完整文件名

    Returns:
        文件名, 后缀名
        example:
            xxx, .jpg

    """
    pach, filename = os.path.split(filestr)
    return os.path.splitext(filename)


def FileExtLegitimate(ext, uploadtype):
    """判断文件类型是否允许上传

    image支持的类型: ['.jpeg', '.jpg', '.png', '.jpg']
    video支持的类型: ['.mp4', '.avi']

    Args:
        ext: str, 后缀名
        uploadtype: str, 检验类型 如 image

    Returns:
        如果检验的后缀名存在支持类型里面 返回True 不存在返回False
        example:
            if not FileExtLegitimate(".mp4", 'image'):
                return 400, '文件类型不允许', {}

    """
    if ext:
        if uploadtype == 'image':
            if str(ext) not in ['.jpeg', '.jpg', '.png', '.jpg']:
                return False
            else:
                return True

        elif uploadtype == 'video':
            if str(ext) not in ['.mp4', '.avi']:
                return False
            else:
                return True

        return False

    else:
        return False


def upload_file(request):

    try:
        file = request.files['file']
    except:
        return 400, '错误: 没有文件', ''

    upload_key = request.form.get('uploadKey', None)
    if not upload_key:
        return 400, '错误: Key值不能为空', {}

    if upload_key not in UPLOADFILE_CONFIG:
        return 400, '错误: 不允许使用的Key值', {}

    filename, ext = QueryFileName(file.filename)
    if not FileExtLegitimate(ext, 'image'):
        return 400, '文件类型不允许', {}
    newfilename = CreateNewFilename(ext)

    # 根据不同的上传标签制定不停的文件处理流
    if upload_key in ['userhead']:
        files = FileCompress.HeadImg(file)
    else:
        files = file

    # 保存文件到服务器
    files.save(os.path.join(os.path.abspath('app/static/' +
                                            UPLOADFILE_CONFIG[str(upload_key)] + "/"), newfilename))

    # 需要生成缩略图的
    if upload_key == 'photo':
        FileCompress.HeadImg(request.files['file']).save(
            os.path.join(os.path.abspath('app/static/'), newfilename))

    # 加载地址
    try:
        LOADPATH = config[AppRAM.runConfig].STATIC_LOADPATH

    except Exception as e:
        print(e)
        LOADPATH = ""

    return 200, 'ok', {
        'lodpath': LOADPATH + '/static' + UPLOADFILE_CONFIG[str(upload_key)] + '/' + newfilename,
        'ospath': UPLOADFILE_CONFIG[str(upload_key)] + '/' + newfilename,
        'filename': newfilename
    }
