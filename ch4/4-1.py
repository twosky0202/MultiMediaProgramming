import cv2 as cv

# 에지 연산자
# img = cv.imread('soccer.jpg')
img = cv.imread('check.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = cv.blur(gray, (3, 3))  # 잡음 제거 효과

# 소벨 연산자 적용
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)  # gray 이미지만 가능. 음수 포함 위해 32비트로 바꿔줌. 3, 4번째 인자 1, 0 -> sobel_x
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)  # 3, 4번째 인자 0, 1 -> sobel_y
grad = cv.Laplacian(gray, cv.CV_32F)

# sobel_x = cv.convertScaleAbs(grad_x)  # 행렬의 음수 값을 절대값을 취해 양수 영상으로 변환
# sobel_y = cv.convertScaleAbs(grad_y)
lap = cv.convertScaleAbs(grad)

# edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)  # 에지 강도 계산. 두 비율의 합이 1이 되게
# 0.5 * sobel_x + 0.5 * sobel_y + 0.0

cv.imshow('Original', gray)
# cv.imshow('sobelx', sobel_x)
# cv.imshow('sobely', sobel_y)
# cv.imshow('edge strength', edge_strength)
cv.imshow('laplacian', lap)

cv.waitKey()
cv.destroyAllWindows()
