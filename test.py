import base64
import random
import requests
import cv2 as cv
import numpy as np

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
}
yzm_url = f"https://www.icris.cr.gov.hk/csci/shwcaptcha.do?checkPoint=login&rand={random.random()}"
content = requests.get(url=yzm_url, headers=headers).content
with open('img1.png', 'wb') as w:
    w.write(content)
print(base64.b64encode(content))
img = cv.imread('img1.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite("img2.png", gray)

def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):  # 加高斯噪声
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])


src = cv.imread('img2.png')
dst = cv.GaussianBlur(src, (5, 5), 0)  # 高斯模糊
cv.imwrite("img3.png", dst)

