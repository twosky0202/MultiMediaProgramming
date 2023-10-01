import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg')
h=cv.calcHist([img],[2],None,[256],[0,256]) # 2번 채널인 R 채널에서 히스토그램 구함
plt.plot(h,color='r',linewidth=1) # r : 빨간색

h=cv.calcHist([img],[1],None,[256],[0,256]) # 1번 채널인 G 채널에서 히스토그램 구함
plt.plot(h,color='g',linewidth=2, linestyle='dotted')

h=cv.calcHist([img],[0],None,[256],[0,256]) # 0번 채널인 B 채널에서 히스토그램 구함
plt.plot(h,color='b',linewidth=3, linestyle='dashed')

plt.show()