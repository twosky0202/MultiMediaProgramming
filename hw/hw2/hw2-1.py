import cv2 as cv

img = cv.imread('soccer.jpg')
cv.imshow('original', img)

while True:
    key = cv.waitKey(0)

    if key == ord('y'):
        # YCbCr 컬러 모델로 변환
        ycbcr_frame = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
        # YCbCr 범위로 피부색을 검출
        skin_color_mask = cv.inRange(ycbcr_frame, (0, 133, 77), (255, 173, 127))
        # 피부색 부분만 출력
        img_skin_color = cv.bitwise_and(img, img, mask=skin_color_mask)
        cv.imshow('Skin Color Detection (YCbCr)', img_skin_color)

    elif key == ord('h'):
        # HSV 컬러 모델로 변환
        hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        # HSV 범위로 피부색을 검출
        skin_color_mask = cv.inRange(hsv_img, (0, 70, 50), (50, 150, 255))
        # 피부색 부분만 출력
        img_skin_color = cv.bitwise_and(img, img, mask=skin_color_mask)
        cv.imshow('Skin Color Detection (HSV)', img_skin_color)

    elif key == ord('q'):
        cv.destroyAllWindows()
        break
