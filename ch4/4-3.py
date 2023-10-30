import cv2 as cv
import numpy as np

# 경계선 찾기(Contours)
img = cv.imread('soccer.jpg')  # 영상 읽기
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# canny = cv.Canny(gray, 100, 200)  # 에지 이미지

t, bin_gray = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)  # 이진 영상
# contour, hierarchy = cv.findContours(bin_gray, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contour, hierarchy = cv.findContours(bin_gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

lcontour = []
for i in range(len(contour)):  # 너무 짧으면 의미있는 경계선 아님
    if contour[i].shape[0] > 100:  # 길이가 100보다 크면. 각각의 경계선은 에지 픽셀로 구성되어 있음
        lcontour.append(contour[i])

cv.drawContours(img, lcontour, -1, (0, 255, 0), 3)  # 길이 100 이상 contour만
# cv.drawContours(img, contour, -1, (0, 255, 0), 3)  # 모든 contour(길이 100이하 포함)

cv.imshow('Original with contours', img)
# cv.imshow('Canny', canny)
cv.imshow('Otsu binarization', bin_gray)

cv.waitKey()
cv.destroyAllWindows()
