import cv2 as cv
import sys

img = cv.imread('soccer.jpg') # 영상 읽기
print(type(img)) # numpy.ndarray
print(img.shape) # (948, 1434, 3) 이미지 세로 크기, 이미지 가로 크기, 한 픽셀을 표현하는 데 필요한 바이트 수 - 3 : color(rgb)

print(img[850][50][0], img[850][50][1], img[850][50][2])
print(img[450][500][0], img[450][500][1], img[450][500][2])
print(img[450][1000][0], img[450][1000][1], img[450][1000][2])


if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display', img) # 윈도우에 영상 표시(타이틀 이름, 표시할 영상)

cv.waitKey() # 아무 키 들어왔을 때 종료
cv.destroyAllWindows() # 지금까지 만든 모든 윈도우 닫기