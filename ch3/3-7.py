import cv2 as cv
import numpy as np

# 영역 처리
img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize=(0, 0), fx=0.4, fy=0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.putText(gray, 'soccer', (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv.imshow('Original', gray)

# 가우시안 필터. 스무딩/블러링 필터
smooth = np.hstack((cv.GaussianBlur(gray, (5, 5), 0.0), cv.GaussianBlur(gray, (9, 9), 0.0),
                    cv.GaussianBlur(gray, (15, 15),
                                    0.0)))  # 필터 크기(ex.(5, 5), (9, 9)) 제공해주면 GaussianBlur에서 계산을 해줌. 0.0 : 시그마값. 특별한 언급이 없는 한 0.0 넣어주기
cv.imshow('Smooth', smooth)

# 엠보싱 필터
femboss = np.array([[-1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0]])

gray16 = np.int16(gray)  # gray는 1바이트(8bits) => 16bits
emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))  # 0~255 값만 표현
emboss_bad = np.uint8(cv.filter2D(gray16, -1, femboss) + 128)
emboss_worse = cv.filter2D(gray, -1, femboss)

cv.imshow('Emboss', emboss)
cv.imshow('Emboss_bad', emboss_bad)
cv.imshow('Emboss_worse', emboss_worse)

cv.waitKey()
cv.destroyAllWindows()
