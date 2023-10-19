import cv2 as cv

# 허프 변환 - 원 검출
img = cv.imread('apples.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 그레이 영상

apples = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 200, param1=150, param2=20, minRadius=50, maxRadius=120)

for i in apples[0]:
    cv.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255, 0, 0), 2)

cv.imshow('Apple detection', img)

cv.waitKey()
cv.destroyAllWindows()
