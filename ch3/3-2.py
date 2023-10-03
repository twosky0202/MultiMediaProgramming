import cv2 as cv
import matplotlib.pyplot as plt

# 히스토그램
img = cv.imread('soccer.jpg')
h = cv.calcHist([img], [2], None, [256], [0, 256])  # 2번 채널인 R 채널에서 히스토그램 구함
plt.plot(h, color='r', linewidth=1)  # r : 빨간색, linestyle default type : 실선

hg = cv.calcHist([img], [1], None, [256], [0, 256])  # 1번 채널인 G 채널에서 히스토그램 구함
plt.plot(hg, color='g', linewidth=2, linestyle='dotted')  # 점선

hb = cv.calcHist([img], [0], None, [256], [0, 256])  # 0번 채널인 B 채널에서 히스토그램 구함
plt.plot(hb, color='b', linewidth=3, linestyle='dashed')  # 파선

plt.show()
