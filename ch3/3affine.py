import cv2 as cv
import numpy as np

img = cv.imread('rose.png')

rows, cols = img.shape[:2]  # shape은 영상의 크기(세로, 가로)

# 좌우 대칭
src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
dst_points = np.float32([[cols - 1, 0], [0, 0], [cols - 1, rows - 1]])

# 상하 대칭
src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
dst_points = np.float32([[0, rows - 1], [cols - 1, rows - 1], [0, 0]])

# 원점 대칭
src_points = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
dst_points = np.float32([[cols - 1, rows - 1], [cols - 1, 0], [0, rows - 1]])

# 90 반시계방향 rotate
src_points = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
dst_points = np.float32([[0, cols - 1], [rows - 1, cols - 1], [0, 0]])

affine_matrix = cv.getAffineTransform(src_points, dst_points)
# img_symmetry = cv.warpAffine(img, affine_matrix, (cols, rows))  # 3번째 인자는 출력 영상의 크기(가로, 세로)
img_symmetry = cv.warpAffine(img, affine_matrix, (rows, cols))  # 반시계 방향 rotate

cv.imshow('Original', img)
cv.imshow('Symmetry', img_symmetry)

cv.waitKey()
cv.destroyAllWindows()
