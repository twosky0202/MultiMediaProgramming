import cv2 as cv
import numpy as np

img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.float32)  # 10x10 삼각형 모양 영상

ux = np.array([[-1, 0, 1]])  # 1차 미분 - x 필터
uy = np.array([-1, 0, 1]).transpose()  # 1차 미분 - y 필터. transpose() : 행과 열을 바꿈
k = cv.getGaussianKernel(3, 1)  # 가우시안 필터 준비
g = np.outer(k, k.transpose())  # 가우시안 필터. gaussionBlur를 꼭 쓸 필요는 없음

dy = cv.filter2D(img, cv.CV_32F, uy)  # 컨볼루션 함수
dx = cv.filter2D(img, cv.CV_32F, ux)
dyy = dy * dy
dxx = dx * dx
dyx = dy * dx
gdyy = cv.filter2D(dyy, cv.CV_32F, g)  # p
gdxx = cv.filter2D(dxx, cv.CV_32F, g)  # q
gdyx = cv.filter2D(dyx, cv.CV_32F, g)  # r
C = (gdyy * gdxx - gdyx * gdyx) - 0.04 * (gdyy + gdxx) * (gdyy + gdxx)  # k == 0.04

for j in range(1, C.shape[0] - 1):  # 비최대 억제
    for i in range(1, C.shape[1] - 1):
        if C[j, i] > 0.1 and sum(sum(C[j, i] > C[j - 1:j + 2, i - 1:i + 2])) == 8:  # 나를 둘러싸고 있는 8개 픽셀보다 큰 경우
            img[j, i] = 9  # 특징점을 원본 영상에 9로 표시

np.set_printoptions(precision=2)
print(dy)
print(dx)
print(dyy)
print(dxx)
print(dyx)
print(gdyy)
print(gdxx)
print(gdyx)
print(C)  # 특징 가능성 맵
print(img)  # 특징점을 9로 표시한 원본 영상

popping = np.zeros([160, 160], np.uint8)  # 화소 확인 가능하게 16배로 확대
for j in range(0, 160):
    for i in range(0, 160):
        popping[j, i] = np.uint8((C[j // 16, i // 16] + 0.06) * 700)

cv.imshow('Image Display2', popping)
cv.waitKey()
cv.destroyAllWindows()
