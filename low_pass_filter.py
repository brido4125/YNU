import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('산군.jpeg')


# Mean Filter
def mean_filter():
    # 10 by 10 크기의 필터 사용
    blur = cv2.blur(img, (10, 10))

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Blurred By Mean')
    plt.xticks([]), plt.yticks([])
    plt.show()


# Median Filter 위한 noise 추가
def salt_and_pepper():
    noise = img.copy()
    height, width, channel = img.shape
    salt = int(height * width * channel * 0.1)
    for i in range(salt):
        row = int(np.random.randint(99999, size=1) % height)
        col = int(np.random.randint(99999, size=1) % width)
        ch = int(np.random.randint(99999, size=1) % channel)
        noise[row][col][ch] = 255 if np.random.randint(99999, size=1) % 2 == 1 else 0
    return noise


# Median Filter
def median_filter():
    clear = cv2.medianBlur(salt_and_pepper(), 5)

    plt.subplot(121), plt.imshow(salt_and_pepper()), plt.title('Salt and Pepper')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(clear), plt.title('Blurred By Median')
    plt.xticks([]), plt.yticks([])
    plt.show()


def img_to_gray(image):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)
    return out


# Laplacian Filer
def laplacian_filter(image):
    image = img_to_gray(image)
    laplacian_img = cv2.Laplacian(image, cv2.CV_8U, ksize=3)

    plt.subplot(121), plt.imshow(image), plt.title('Gray Scale Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(laplacian_img), plt.title('Laplacian')
    plt.xticks([]), plt.yticks([])
    plt.show()


mean_filter()
median_filter()
laplacian_filter(img)
