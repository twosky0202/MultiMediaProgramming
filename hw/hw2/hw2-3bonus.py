import cv2 as cv
import numpy as np

img = cv.imread('rose.png')
rows, cols = img.shape[:2]  # shape은 영상의 크기(세로, 가로)
img_rotate = img


def click(event, x, y, flags, param):
    global img_rotate, img, cols, rows
    if event == cv.EVENT_LBUTTONDOWN:  # 시계 반대 방향
        src_points = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
        dst_points = np.float32([[0, cols - 1], [rows - 1, cols - 1], [0, 0]])
        affine_matrix = cv.getAffineTransform(src_points, dst_points)
        img_rotate = cv.warpAffine(img, affine_matrix, (rows, cols))
        img = img_rotate
        cols, rows = rows, cols
    elif event == cv.EVENT_RBUTTONDOWN:  # 시계 방향
        src_points = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
        dst_points = np.float32([[rows - 1, 0], [0, 0], [rows - 1, cols - 1]])
        affine_matrix = cv.getAffineTransform(src_points, dst_points)
        img_rotate = cv.warpAffine(img, affine_matrix, (rows, cols))
        img = img_rotate
        cols, rows = rows, cols
    cv.imshow('Rotate', img_rotate)


cv.namedWindow('Rotate')
cv.imshow('Rotate', img_rotate)
cv.setMouseCallback('Rotate', click)

while True:
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
