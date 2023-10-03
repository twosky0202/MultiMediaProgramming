import cv2 as cv

# 오츄(Otsu) 알고리즘
# img = cv.imread('soccer.jpg')
gray = cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)

# t, bin_img = cv.threshold(img[:, :, 2], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
t, bin_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)  # 자동으로 적절한 임계값을 찾아서 그 임계값으로 이진화한 영상 리턴
print('오츄 알고리즘이 찾은 최적 임곗값=', t)

# cv.imshow('R channel', img[:, :, 2])  # R 채널 영상
cv.imshow('Gray', gray)  # gray 영상
cv.imshow('binarization', bin_img)  # 이진화 영상

cv.waitKey()
cv.destroyAllWindows()
