import cv2 as cv

# inRange
# gray = cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)  # gray 영상
# cv.imshow('original - gray', gray)

# gray_mask = cv.inRange(gray, 120, 170)    # 두 값 제시. 120 ~ 170이면 white, 아니면 black
# cv.imshow('inRange', gray_mask)

img = cv.imread('soccer.jpg')  # color 영상
cv.imshow('original', img)

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # 사람이 느끼는 색상 범위를 표현할 때는 rgb보다는 명도와 채도가 있는 hsv로 표현
red_mask = cv.inRange(hsv_img, (-10, 50, 50), (10, 255, 255))  # 통상적으로 hsv에서 red의 범위
img_red = cv.bitwise_and(img, img, mask=red_mask)  # and 연산자. black(0)으로 되어있으면 0으로, white(1)로 되어있으면(빨간색 범위에 있는 픽셀) img 값 그대로 출력
# A and B : if B=0, 0, else if B=1, (A=0 -> 0, A=1 -> 1)

# cv.imshow('red detection', red_mask) # red 부분
cv.imshow('red detection', img_red)

cv.waitKey()
cv.destroyAllWindows()
