import skimage
import numpy as np
import cv2 as cv

orig = skimage.data.horse()  # 배경 1, 물체 0(black)
img = 255 - np.uint8(orig) * 255  # 0/1 -> 0/255 -> 255/0 (255에서 빼주기)
cv.imshow('Horse', img)

contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

img2 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # 컬러 디스플레이용 영상
cv.drawContours(img2, contours, -1, (255, 0, 255), 2)
cv.imshow('Horse with contour', img2)

contour = contours[0]
print(contour.shape)

m = cv.moments(contour)  # 몇 가지 특징
print(m)

area = cv.contourArea(contour)
cx, cy = m['m10'] / m['m00'], m['m01'] / m['m00']
perimeter = cv.arcLength(contour, True)
roundness = (4.0 * np.pi * area) / (perimeter * perimeter)
print('면적=', area, '\n중점=(', cx, ',', cy, ')', '\n둘레=', perimeter, '\n둥근 정도=', roundness)

img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # 컬러 디스플레이용 영상

contour_approx = cv.approxPolyDP(contour, 8, True)  # 직선 근사. 픽셀의 개수가 적을수록 일반화된 도형
cv.drawContours(img3, [contour_approx], -1, (0, 255, 0), 2)
print(contour_approx.shape)
contour_approx = cv.approxPolyDP(contour, 20, True)  # 직선 근사. 숫자가 크면 클수록 선택된 화소의 개수가 적음 -> 모양이 더 대략적인 결과
cv.drawContours(img3, [contour_approx], -1, (255, 255, 0), 2)
print(contour_approx.shape)

hull = cv.convexHull(contour)  # 볼록 헐. 볼록 다각형. 하나도 움푹 들어가지 않게끔
cv.drawContours((img3, [hull], -1, (0, 0, 255), 2))
print(hull.shape)

rehull = hull.reshape(1, hull.shape[0], hull.shape[2])  # 행렬에 대한 형태를 바꿈
cv.drawContours(img3, rehull, -1, (0, 0, 255), 2)

cv.imshow('Horse with line segments and convex hull', img3)

cv.waitKey()
cv.destroyAllWindows()
