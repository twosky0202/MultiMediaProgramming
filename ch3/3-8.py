import cv2 as cv

img = cv.imread('rose.png')
patch = img[250:350, 170:270, :]  # 일부만 자름 -> 5배씩 확대

img = cv.rectangle(img, (170, 250), (270, 350), (255, 0, 0), 3)
patch1 = cv.resize(patch, dsize=(0, 0), fx=11, fy=11, interpolation=cv.INTER_NEAREST)  # nearest neighbor 방법
patch2 = cv.resize(patch, dsize=(0, 0), fx=11, fy=11, interpolation=cv.INTER_LINEAR)  # 양선형 보간법
patch3 = cv.resize(patch, dsize=(0, 0), fx=11, fy=11, interpolation=cv.INTER_CUBIC)  # 3차 회선 보간법

cv.imshow('Original', img)
cv.imshow('Resize nearest', patch1)
cv.imshow('Resize bilinear', patch2)
cv.imshow('Resize bicubic', patch3)

cv.waitKey()
cv.destroyAllWindows()
