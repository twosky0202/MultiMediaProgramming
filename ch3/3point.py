import cv2 as cv
import sys
import numpy as np

img = cv.imread('soccer.jpg')
# 1
gray = cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)  # BGR 컬러 영상을 명암 영상으로 변환하여 저장

if gray is None:
    sys.exit('파일을 찾을 수 없습니다.')

# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)	# BGR 컬러 영상을 명암 영상으로 변환
gray_small = cv.resize(gray, dsize=(0, 0), fx=0.25, fy=0.25)  # 이미지를 1/4fh 줄임

cv.imshow('soccer-gray', gray_small)
print(gray_small.shape)  # (237, 358)

# 2. 사칙연산 -> 두 영상의 크기가 같아야함. 결과가 배열
img_plus = cv.add(gray_small, 50)  # y = x + 50
img_minus = cv.subtract(gray_small, 50)  # y = x - 50
img_multi = cv.multiply(gray_small, 2)  # y = 2 * x
img_div = cv.divide(gray_small, 2)  # y = x / 2
pp = np.hstack((img_plus, img_minus, img_multi, img_div))  # hstack은 높이(세로)가 같아야 함
# cv.imshow('point processing', pp)

# 3. 사칙연산 연산자
img_plus2 = gray_small + 50  # y = x + 50. 배열 안에 모든 수에 50씩 더함. 클램핑 처리x -> 범위 넘어가는 것들은 까맣게 표시됨
img_minus2 = gray_small - 50  # y = x - 50
img_multi2 = gray_small * 2  # y = 2 * x
img_div2 = gray_small / 2  # y = x / 2
# cv.imshow('test - pus',img_plus2)

# 4. 영상의 특정 위치가 있으면, 함수로 50 더했을 때, 더하기로 50 더했을 때 어떤 결과가 나오나?
print(gray_small[100, 100], img_plus[100, 100], img_plus2[100, 100])  # 72, 122, 122
print(gray_small[180, 80], img_plus[180, 80], img_plus2[180, 80])  # 226, 255, 20 (오버플로우로 엉뚱한 값이 출력)

# 5
# cv.imshow('test',img_minus2)
print(gray_small[100, 100], img_minus[100, 100], img_minus2[100, 100])  # 72, 22, 22
print(gray_small[120, 180], img_minus[120, 180], img_minus2[120, 180])  # 27, 0, 233

# 6. 영상끼리 더하기 가능
img512 = cv.resize(img, dsize=(512, 512))  # opencv_img 크기랑 같게 하기 위해 크기 조정
opencv_img = cv.imread('opencv_logo512.png')
img_plus3 = cv.add(img512, opencv_img)  # 255보다 큰 부분은 화이트 처리
# cv.imshow('two images - add',img_plus3)

# 7. 비율적으로 더하는 함수
img_plus4 = cv.addWeighted(img512, 0.5, opencv_img, 0.5, 0)  # 각각 0.5 비율로 더함
# cv.imshow('two images - addWeighted', img_plus4)

# 8. 역변환
img_rev = cv.subtract(255, gray)  # y = 255 - x
# cv.imshow('reverse image', img_rev)

# 9. 이진 영상
ret, img_binary50 = cv.threshold(gray_small, 50, 255, cv.THRESH_BINARY)  # 임계값 50
# cv.imshow('threshold', img_binary50)

# 임계값 별
ret, img_binary100 = cv.threshold(gray_small, 100, 255, cv.THRESH_BINARY)  # 임계값 100
ret, img_binary150 = cv.threshold(gray_small, 150, 255, cv.THRESH_BINARY)  # 임계값 150
ret, img_binary200 = cv.threshold(gray_small, 200, 255, cv.THRESH_BINARY)  # 임계값 200
img_binary = np.hstack((img_binary50, img_binary100, img_binary150, img_binary200))
# cv.imshow('threshold', img_binary)

# 타입 별
ret, img_binaryB = cv.threshold(gray_small, 100, 255, cv.THRESH_BINARY)
ret, img_binaryBINV = cv.threshold(gray_small, 100, 255, cv.THRESH_BINARY_INV)
ret, img_binaryT = cv.threshold(gray_small, 100, 255, cv.THRESH_TRUNC)
ret, img_binaryT0 = cv.threshold(gray_small, 100, 255, cv.THRESH_TOZERO)
ret, img_binaryT0INV = cv.threshold(gray_small, 100, 255, cv.THRESH_TOZERO_INV)
img_binary2 = np.hstack((img_binaryB, img_binaryBINV, img_binaryT, img_binaryT0, img_binaryT0INV))
cv.imshow('threshold2', img_binary2)

cv.waitKey()
cv.destroyAllWindows()
