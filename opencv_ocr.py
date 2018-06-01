import pytesseract
import cv2
import numpy as np
from PIL import Image

src_path = "f:/temp"

def get_string(img_path):

    # Read
    img = cv2.imread(img_path)
    # 转成灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 去除脏点
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite(src_path + "removed_noise.png", img)
    # threshold 方法是通过遍历灰度图中点，将图像信息二值化，处理过后的图片只有二种色值。
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(src_path + "thres.png", img)
    result = pytesseract.image_to_string(Image.open(scr_path + "thres.png"))

    return result

print("开始解析文字")
print(get_string(src_path))
