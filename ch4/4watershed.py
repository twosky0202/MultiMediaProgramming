import cv2 as cv
import numpy as np

# 영역 분할 - watershed
# Image loading
img = cv.imread("water_coins.jpg")

# image grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Threshold Processing
ret, bin_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)  # 이진화(오츄 알고리즘)
cv.imshow('binarized image', bin_img)

# white(object) noise removal
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
b_opening = cv.dilate(cv.erode(bin_img, kernel, iterations=2), kernel, iterations=2)  # 열기(침식->팽창)
cv.imshow('white noise removal', b_opening)

# sure background area
sure_bg = cv.dilate(b_opening, kernel, iterations=3)  # 3픽셀만큼 팽창
cv.imshow('sure background area', sure_bg)

# sure foreground area
# distanceTransform : Binary 이미지에서  픽셀값이 0인 배경으로부터의 거리를 픽셀값이 255인 영역에 표현하는 방법
dist_transform = cv.distanceTransform(b_opening, cv.DIST_L2, 5)
# 2 : 거리 공식
# 3 : 마스크 크기
dist = dist_transform * 10  # 시각적으로 보기 위해 값을 키움
dist = np.uint8(dist)  # 한바이트 단위로 바꿈
cv.imshow('dist_transform', dist)

ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
cv.imshow('sure foreground area', sure_fg)

# unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)  # 확실하게 배경 - 확실하게 물체
cv.imshow('unknown region', unknown)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)  # 각 connectedComponent마다 0부터 숫자 부여. 배경 0 물체 1이상 정수
# Add one to all labels so that sure background is not 0, but 1
markers = markers + 1  # 배경을 0으로 보지 말고 배경도 하나의 영역이기 때문에 1의 값을 줌
# Now, mark the region of unknown with zero
markers[unknown == 255] = 0  # unknown을 0으로

markers = cv.watershed(img, markers)  # watershed : 물을 채워가면서 unknown을 connectedComponent 숫자 부여
img[markers == -1] = [255, 0, 0]  # 워터쉐드에 의해 두 영역이 만나는 지점의 마커 값 -1 저장 & 파란색 표시
cv.imshow("watershed results", img)  # 물체들이 붙어있다 하더라도 동전 하나하나 잘 분리됨

cv.waitKey()
cv.destroyAllWindows()
