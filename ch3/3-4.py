import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 모폴로지
# img = cv.imread('JohnHancocksSignature.png', cv.IMREAD_UNCHANGED)
img = cv.imread('morph.jpg', cv.IMREAD_GRAYSCALE)

# t, bin_img = cv.threshold(img[:, :, 3], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)  # 이진 영상
t, b = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plt.imshow(b, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# b = bin_img[bin_img.shape[0] // 2:bin_img.shape[0], 0:bin_img.shape[0] // 2 + 1]  # 일부만 잘라서 사용
# plt.imshow(b, cmap='gray'), plt.xticks([]), plt.yticks([])
# plt.show()

se = np.uint8([[0, 0, 1, 0, 0],  # 구조 요소 포함 여부 언급 목적
               [0, 1, 1, 1, 0],  # -> Convolution 연산 아님
               [1, 1, 1, 1, 1],
               [0, 1, 1, 1, 0],
               [0, 0, 1, 0, 0]])

b_dilation = cv.dilate(b, se, iterations=1)  # 팽창 (입력영상, 구조 요소, 반복 횟수)
# plt.imshow(b_dilation, cmap='gray'), plt.xticks([]), plt.yticks([])
# plt.show()

b_erosion = cv.erode(b, se, iterations=1)  # 침식
# plt.imshow(b_erosion, cmap='gray'), plt.xticks([]), plt.yticks([])
# plt.show()

b_closing = cv.erode(cv.dilate(b, se, iterations=1), se, iterations=1)  # 닫힘 : 팽창 -> 침식
# plt.imshow(b_closing, cmap='gray'), plt.xticks([]), plt.yticks([])
# plt.show()

b_opening = cv.dilate(cv.erode(b, se, iterations=1), se, iterations=1)  # 열림 : 침식 -> 팽창
# plt.imshow(b_opening, cmap='gray'), plt.xticks([]), plt.yticks([])
# plt.show()

morph = np.hstack((b, b_dilation, b_erosion, b_closing, b_opening))
cv.imshow('morph', morph)

cv.waitKey()
cv.destroyAllWindows()