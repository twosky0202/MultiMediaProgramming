import cv2 as cv
import numpy as np

# 영역 처리
img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize=(0, 0), fx=0.4, fy=0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.putText(gray, 'soccer', (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
# cv.imshow('Original', gray)

# 가우시안 필터. 스무딩/블러링 필터
smooth = np.hstack((cv.GaussianBlur(gray, (5, 5), 0.0), cv.GaussianBlur(gray, (9, 9), 0.0),
                    cv.GaussianBlur(gray, (15, 15),
                                    0.0)))  # 필터 크기(ex.(5, 5), (9, 9)) 제공해주면 GaussianBlur에서 계산을 해줌. 0.0 : 시그마값. 특별한 언급이 없는 한 0.0 넣어주기
# cv.imshow('Smooth', smooth)

# 엠보싱 필터
femboss = np.array([[-1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0]])

gray16 = np.int16(gray)  # gray는 1바이트(8bits) => 16bits
emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))  # 0~255 값만 표현
emboss_bad = np.uint8(cv.filter2D(gray16, -1, femboss) + 128)
emboss_worse = cv.filter2D(gray, -1, femboss)

# cv.imshow('Emboss', emboss)
# cv.imshow('Emboss_bad', emboss_bad)
# cv.imshow('Emboss_worse', emboss_worse)

# 평균값 필터
faverage = np.array([[1.0/9.0, 1.0/9.0, 1.0/9.0],
                    [1.0/9.0, 1.0/9.0, 1.0/9.0],
                    [1.0/9.0, 1.0/9.0, 1.0/9.0]])

# 샤프닝 필터 - 전체 합 0 -> 경계선만
fsharpening1 = np.array([[0.0, -1.0, 0.0],
                        [-1.0, 4.0, -1.0],
                        [0.0, -1.0, 0.0]])

# 샤프닝 필터 - 전체 합 1 -> 원래 이미지에 경계선 추가
fsharpening2 = np.array([[0.0, -1.0, 0.0],
                        [-1.0, 5.0, -1.0],
                        [0.0, -1.0, 0.0]])

result = cv.filter2D(gray, -1, faverage)
# result = cv.filter2D(gray, -1, fsharpening1)
# result = cv.filter2D(gray, -1, fsharpening2)
# cv.imshow('result', result)

gray = cv.imread('coins.png', cv.IMREAD_GRAYSCALE)

# 평균값 필터 - 함수 사용
average = cv.blur(gray, (9, 9))
cv.imshow('result - average', average) # faverage와 똑같은 필터

# 중간값 필터
median = cv.medianBlur(gray, 3)
cv.imshow('result - median', median)

bilateral = cv.bilateralFilter(gray, -1, sigmaColor=5, sigmaSpace=5)
# 각 픽셀과 주변 요소들로부터 가중 평균을 구함 => 가우시안과 유사
# 단, 픽셀값의 차이도 같이 사용하여 유사한 픽셀에 더 큰 가중치를 두는 방법
# 경계선을 유지하며 스무딩
cv.imshow('result - bilateral', bilateral)

cv.waitKey()
cv.destroyAllWindows()
