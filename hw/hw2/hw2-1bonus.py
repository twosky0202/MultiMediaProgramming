import cv2 as cv
import sys

cap = cv.VideoCapture('face2.mp4')

if not cap.isOpened():
    sys.exit('카메라 연결 실패')


while True:
    ret, frame = cap.read()

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    ycbcr_frame = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)
    skin_color_mask = cv.inRange(ycbcr_frame, (0, 133, 77), (255, 173, 127))
    img_skin_color = cv.bitwise_and(frame, frame, mask=skin_color_mask)
    cv.imshow('Skin Color Detection', img_skin_color)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
