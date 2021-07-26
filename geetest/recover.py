# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/7/26 15:58
@Software: PyCharm
@File    : recover.py
图片重组
'''
from PIL import Image


def deal_pic(img,imgname):
    captcha = Image.new('RGB', (12, 80))
    img = Image.open(img)
    # 将图片裁剪为52份
    for i in range(52):
        if i < 26:
            box = (i * 12, 0, (i + 1) * 12, 80)
        else:
            box = ((i - 26) * 12, 80, (i - 25) * 12, 160)
        regoin = img.crop(box)
        captcha.paste(regoin, (0, 0))
        captcha.save(f'{i}.jpg')
    captcha = Image.new('RGB', (10 * 26, 80 * 2))
    data = {0: 39, 1: 38, 2: 48, 3: 49, 4: 41, 5: 40, 6: 46, 7: 47, 8: 35, 9: 34, 10: 50, 11: 51, 12: 33, 13: 32,
            14: 28, 15: 29,
            16: 27, 17: 26, 18: 36, 19: 37, 20: 31, 21: 30, 22: 44, 23: 45,
            24: 43, 25: 42, 26: 12, 27: 13, 28: 23, 29: 22, 30: 14, 31: 15, 32: 21, 33: 20, 34: 8, 35: 9, 36: 25,
            37: 24, 38: 6,
            39: 7, 40: 3, 41: 2, 42: 0, 43: 1, 44: 11, 45: 10, 46: 4, 47: 5, 48: 19, 49: 18, 50: 16, 51: 17}
    # 将52份图片重新组合（注意将每张图片的宽度由12裁剪为10）
    for i, j in data.items():
        if i < 26:
            regoin = Image.open(f'{j}.jpg').crop((0, 0, 10, 80))
            captcha.paste(regoin, (i * 10, 0, (i + 1) * 10, 80))
        else:
            regoin = Image.open(f'{j}.jpg').crop((0, 0, 10, 80))
            captcha.paste(regoin, ((i - 26) * 10, 80, (i - 25) * 10, 160))
    captcha.save(f'{imgname}.jpg')