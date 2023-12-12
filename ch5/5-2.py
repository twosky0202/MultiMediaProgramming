import cv2 as cv

img = cv.imread('mot_color70.jpg')  # 영상 읽기
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # gray 영상으로 바꿔줌

sift = cv.SIFT_create()  # sift 계산을 할 수 있는 객체
kp, des = sift.detectAndCompute(gray, None)  # return 값 : keypoint, 기술
print(len(kp))
print(kp[0].pt, kp[0].size, kp[0].octave, kp[0].angle)
print(des[0])


gray = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # 어떤 방식으로 그릴지 다양한 flag 제공
cv.imshow('sift', gray)

k = cv.waitKey()
cv.destroyAllWindows()
